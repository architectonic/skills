#!/usr/bin/env python3
"""
enrich_dist_skills.py — Non-mutating enrichment pass over dist/skills.

Reads every SKILL.md, derives tags/domain/risk, dedupes tags, fingerprints
source family, and writes proposal-only reports. Does NOT modify any skill.

Outputs:
  reports/dist-skills-enriched-inventory.json
  reports/dist-skills-domain-report.md
  reports/dist-skills-risk-report.md
  reports/frontmatter-proposals.json
  reports/frontmatter-proposals.md
  reports/quality-gate-flagged.json
  reports/source-fingerprint.md
"""
from pathlib import Path
from collections import Counter, defaultdict
import json
import re
import yaml
from typing import Iterable

ROOT = Path("dist/skills")
OUT = Path("reports")
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# YAML frontmatter parser (pyyaml-backed)
# ---------------------------------------------------------------------------

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)


def parse_frontmatter(text: str):
    """Return (frontmatter_dict, body_text) using yaml.safe_load."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1))
        if not isinstance(fm, dict):
            fm = {}
    except yaml.YAMLError:
        fm = {}
    body = text[m.end():]
    return fm, body


def slug_to_title(value: str) -> str:
    text = value.replace("_", " ").replace("-", " ").strip()
    text = re.sub(r"\s+", " ", text)
    if not text:
        return value
    words = []
    for word in text.split():
        if word.isupper():
            words.append(word)
        elif len(word) <= 3 and word.lower() in {"api", "cli", "sdk", "css", "html", "sql", "aws", "gcp"}:
            words.append(word.upper())
        else:
            words.append(word.capitalize())
    return " ".join(words)


def first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            heading = line[2:].strip()
            heading = re.sub(r"\s+\([^)]*\)$", "", heading).strip()
            return heading
    return ""


def first_meaningful_paragraph(body: str) -> str:
    lines = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            if lines:
                break
            continue
        if line.startswith("#") or line.startswith(">") or line.startswith("```") or line.startswith("<!--"):
            continue
        if line.startswith("|") or re.match(r"^[-*]\s", line):
            continue
        lines.append(line)
        if len(" ".join(lines)) >= 220:
            break
    paragraph = " ".join(lines).strip()
    paragraph = re.sub(r"\s+", " ", paragraph)
    return paragraph


TAG_RENAMES = {
    "agent-skill": "skill",
    "software-development": "software-engineering",
}


def normalize_tags(tags: Iterable[str], domain: str) -> list[str]:
    normalized = []
    seen = set()
    for tag in tags:
        value = str(tag).strip().lower()
        if not value:
            continue
        value = TAG_RENAMES.get(value, value)
        if value not in seen:
            seen.add(value)
            normalized.append(value)
    if domain and domain not in seen:
        normalized.insert(0, domain)
        seen.add(domain)
    if "okf" not in seen:
        normalized.append("okf")
    return normalized


# ---------------------------------------------------------------------------
# Domain / risk keyword rules
# ---------------------------------------------------------------------------

DOMAIN_RULES = {
    "security-offensive": [
        "abusing", "attacking", "exploit", "privesc", "privilege escalation",
        "credential access", "phishing", "mimikatz", "cobalt strike",
        "shadow credentials", "kerberoasting", "pass-the-hash", "red team",
        "offensive", "lateral movement", "persistence", "command and control",
        "c2", "reverse shell", "shellcode", "injection", "sql injection",
        "xss", "csrf", "buffer overflow", "heap spray", "rop chain",
        "keylogger", "rootkit", "bootkit", "ransomware", "worm",
        "trojan", "backdoor", "impersonation", "spoofing", "mitm",
        "man-in-the-middle", "session hijacking", "token theft",
        "pass-the-ticket", "golden ticket", "silver ticket", "diamond ticket",
        "dcsync", "dcshadow", "adcs", "certipy", "pywhisker", "whisker",
        "sharpdpapi", "sharpchrome", "mimikatz", "bloodhound", "rubeus",
        "impacket", "crackmapexec", "evil-winrm", "metasploit", "cobalt",
        "covenant", "sliver", "brute ratel", "sharpup", "certify",
        "scheduled task", "service abuse", "dll hijacking", "dll injection",
        "process hollowing", "process doppelganging", "apc injection",
        "thread execution hijacking", "extra window memory injection",
        "keylogging", "screen capture", "clipboard capture", "shimming",
        "wmi event", "wmi persistence", "bits jobs", "com hijacking",
        "phantom dll", "search order hijacking", "dll proxying",
        "image file execution options", "ifeo", "appinit dlls",
        "appcert dlls", "winlogon helper", "screensaver hijack",
        "accessibility features", "sticky keys", "utilman", "display switch",
        "narrator", "magnification", "on-screen keyboard", "sethc",
        "debugger", "silent process exit", "provlaunch", "aip",
        "winrm", "wmiexec", "smbexec", "atexec", "dcom", "mmc",
        "shell_windows", "powershell", "encoded command", "download cradle",
        "reflective loading", "assembly load", "invoke-expression",
        "iex", "net.webclient", "downloadstring", "downloadfile",
        "start-bitstransfer", "invoke-webrequest", "curl", "wget",
        "amsi bypass", "etw bypass", "patch", "hook", "unhook",
        "direct syscall", "indirect syscall", "hells gate", "halos gate",
        "tartarus gate", "veil", "nightmare", "scarecrow", "donut",
        "process injection", "process doppelgänging", "transacted hollowing",
        "process herpaderping", "inter-process communication", "named pipe",
        "mailslot", "alpc", "window message", "section", "view", "region",
        "file mapping", "view mapping", "low", "medium", "high", "system",
        "trusted installer", "nt authority", "nt \\system", "debug privilege",
        "sebackupprivilege", "serestoreprivilege", "setakeownershipprivilege",
        "sedebugprivilege", "seloaddriverprivilege", "sesecurityprivilege",
        "setcbprivilege", "seundockprivilege", "secreatetokenprivilege",
        "seassignprimarytokenprivilege", "seincreasequotaprivilege",
        "sechangenotifyprivilege", "semanipulateaudithrivilege",
        "seimpersonateprivilege", "secreatepagefileprivilege",
        "secreateglobalprivilege", "sebackupprivilege", "time stomp",
        "timestomp", "mace", "forensic", "anti-forensic", "log clear",
        "event log", "wevtutil", "utilman", "osk", "displayswitch",
        "narrator", "magnify", "atbroker", "sethc", "sethc.exe",
    ],
    "security-defensive": [
        "detecting", "auditing", "monitoring", "incident", "threat",
        "logs", "splunk", "guardduty", "falco", "edr", "ids", "ips",
        "siem", "soar", "xdr", "ndr", "mdr", "mssp", "blue team",
        "defensive", "detection", "prevention", "response", "mitigation",
        "hardening", "baseline", "benchmark", "cis", "stig", "compliance",
        "vulnerability management", "patch management", "risk management",
        "security posture", "attack surface", "exposure", "remediation",
        "threat hunting", "threat intelligence", "ioc", "indicator",
        "yara", "sigma", "snort", "suricata", "zeek", "bro",
        "wireshark", "tcpdump", "network traffic", "packet capture",
        "flow data", "netflow", "sflow", "ipfix", "dns log", "proxy log",
        "firewall log", "vpn log", "auth log", "access log", "error log",
        "application log", "system log", "security log", "audit log",
        "cloudtrail", "azure monitor", "stackdriver", "google cloud audit",
        "aws config", "aws security hub", "aws inspector", "aws macie",
        "aws guardduty", "aws detective", "aws cloudwatch", "azure sentinel",
        "microsoft defender", "sentinelone", "crowdstrike", "carbon black",
        "palo alto", "fortinet", "checkpoint", "sonicwall", "juniper",
        "cisco", "f5", "akamai", "cloudflare", "fastly", "imperva",
        "incident response", "ir", "dfir", "digital forensics",
        "computer forensics", "mobile forensics", "network forensics",
        "memory forensics", "disk forensics", "file forensics",
        "malware analysis", "reverse engineering", "static analysis",
        "dynamic analysis", "sandboxing", "detonation", "behavioral",
        "signature", "heuristic", "anomaly", "baseline", "deviation",
        "drift", "misconfiguration", "exposure", "vulnerability", "cve",
        "cvss", "epss", "kev", "exploitability", "patch tuesday",
        "zero day", "0day", "1day", "n-day", "exploit", "poc",
        "proof of concept", "vulnerability research", "bug bounty",
        "penetration test", "pentest", "red team", "purple team",
        "tabletop", "war game", "simulation", "emulation", "atomic",
        "caldera", "metta", "atomic red team", "prelude", "operator",
        "scythe", "threat emulator", "cobalt strike", "brute ratel",
        "mythic", "havoc", "sliver", "poshc2", "nighthawk", "geacon",
        "supershell", "godzilla", "beacon", "stageless", "malleable",
        "observability", "telemetry", "metrics", "logs", "traces",
        "spans", "events", "exporters", "collectors", "agents",
        "opentelemetry", "otel", "prometheus", "grafana", "loki",
        "tempo", "jaeger", "zipkin", "datadog", "new relic", "dynatrace",
        "honeycomb", "lightstep", "splunk", "elastic", "kibana",
        "logstash", "filebeat", "metricbeat", "packetbeat", "heartbeat",
        "auditbeat", "functionbeat", "journalbeat", "apm", "rum",
        "synthetics", "profiling", "continuous profiling", "pprof",
        "perf", "ebpf", "bpf", "xdp", "tc", "cgroup", "namespace",
        "seccomp", "apparmor", "selinux", "tomo", "landlock",
        "capabilities", "ambient", "bounding", "inheritable", "effective",
        "permitted", "cap_dac_read_search", "cap_net_raw", "cap_sys_ptrace",
        "cap_sys_admin", "cap_net_admin", "cap_net_bind_service",
    ],
    "forensics": [
        "forensics", "disk image", "memory dump", "volatility",
        "autopsy", "amcache", "prefetch", "mft", "pst", "ost",
        "registry", "hive", "ntusr.dat", "usrclass.dat", "sam",
        "evtx", "journal", "ntfs", "e01", "raw", "dd", "dcfldd",
        "dc3dd", "ewfacquire", "ftk imager", "timeline",
        "plaso", "log2timeline", "timesketch", "kape", "triage",
        "acquisition", "chain of custody", "evidence", "exhibit",
        "write blocker", "forensic duplicate", "bit-for-bit",
        "ddrescue", "gddrescue", "hdclone", "acronis", "true image",
        "macrium", "clonezilla", "partimage", "partclone",
        "gparted", "fdisk", "parted", "gdisk", "sfdisk", "cfdisk",
        "diskpart", "diskmgmt", "diskutil", "hdiutil", "vboxmanage",
        "qemu-img", "qemu", "kvm", "libvirt", "virsh", "virt-install",
        "virt-manager", "virt-viewer", "remote-viewer", "spice", "vnc",
        "rdp", "xrdp", "freerdp", "remmina", "vinagre", "tsclient",
        "mstsc", "xfreerdp", "rdesktop", "nx", "x2go", "nomachine",
        "teamviewer", "anydesk", "chrome remote", "splashtop", "logmein",
        "gotoassist", "beyondtrust", "bomgar",
    ],
    "cloud-security": [
        "aws", "azure", "gcp", "kubernetes", "s3", "iam",
        "entra", "office365", "cloud", "ec2", "lambda", "ecs", "eks",
        "guardduty", "cloudtrail", "cloudformation", "azure policy",
        "gcp security command center", "aws security hub", "azure security hub",
        "aws config", "azure monitor", "google cloud audit",
        "iam role", "iam policy", "iam user", "iam group", "iam identity",
        "service account", "workload identity", "oidc federation",
        "cloud security", "cloud audit", "cloud compliance",
        "kubernetes security", "pod security", "container security",
        "serverless security", "lambda security", "api gateway security",
        "s3 bucket", "storage security", "data security",
        "cloud threat", "cloud detection", "cloud incident",
        "infrastructure security", "network security",
    ],
    "agent-operations": [
        "agent", "handoff", "orchestrator", "memory", "operating loop",
        "context", "workflow", "skill", "playbook", "agentic",
        "multi-agent", "swarm", "crew", "delegation", "subagent",
        "sub-agent", "child agent", "parent agent", "coordinator",
        "supervisor", "manager", "worker", "dispatch", "route", "assign",
        "runbook", "playbook", "sop", "procedure", "process", "method",
        "automation", "task scheduling", "state machine",
        "decision tree", "cognitive framework",
    ],
    "software-engineering": [
        "api", "code", "test", "build", "refactor", "architecture",
        "typescript", "python", "react", "next.js", "node", "express",
        "django", "flask", "spring", "rails", "laravel", "database",
        "sql", "nosql", "graphql", "rest", "grpc", "websocket",
        "microservice", "monolith", "serverless", "function", "lambda",
        "docker", "container", "kubernetes", "helm", "terraform",
        "infrastructure", "ci", "cd", "pipeline", "deploy", "release",
        "version", "git", "github", "gitlab", "bitbucket", "branch",
        "merge", "rebase", "commit", "pull request", "code review",
        "lint", "format", "prettier", "eslint", "typecheck", "compile",
        "bundle", "webpack", "vite", "rollup", "esbuild", "turbopack",
        "turborepo", "nx", "lerna", "monorepo", "polyrepo", "workspace",
        "package", "module", "library", "framework", "sdk", "cli",
        "terminal", "shell", "bash", "zsh", "powershell", "cmd",
        "script", "automation", "cron", "schedule", "timer", "trigger",
        "event", "listener", "handler", "callback", "promise", "async",
        "await", "stream", "buffer", "pipe", "transform", "filter",
        "map", "reduce", "sort", "search", "index", "query", "mutation",
        "subscription", "schema", "model", "entity", "dto", "vo",
        "repository", "service", "controller", "middleware", "guard",
        "interceptor", "decorator", "annotation", "metadata", "reflection",
        "dependency injection", "inversion of control", "ioc", "di",
        "factory", "builder", "singleton", "prototype", "adapter",
        "bridge", "composite", "decorator", "facade", "flyweight",
        "proxy", "chain of responsibility", "command", "interpreter",
        "iterator", "mediator", "memento", "observer", "state",
        "strategy", "template method", "visitor", "abstract factory",
        "solid", "dry", "kiss", "yagni", "grasp", "coupling", "cohesion",
        "separation of concerns", "soc", "single responsibility",
        "open-closed", "liskov substitution", "interface segregation",
        "dependency inversion", "clean architecture", "hexagonal",
        "onion", "ports and adapters", "domain-driven design", "ddd",
        "entity", "value object", "aggregate", "domain event",
        "application service", "domain service", "repository",
        "unit of work", "specification", "cqrs", "event sourcing",
        "saga", "process manager", "outbox", "inbox", "idempotency",
        "compensating transaction", "two-phase commit", "2pc",
        "saga pattern", "choreography", "orchestration", "message broker",
        "event bus", "event store", "message queue", "pub/sub",
        "request-reply", "competing consumers", "priority queue",
        "dead letter", "poison message", "retry", "circuit breaker",
        "bulkhead", "timeout", "rate limiting", "throttling",
        "backpressure", "load balancing", "service discovery",
        "health check", "readiness", "liveness", "startup probe",
        "graceful shutdown", "zero-downtime", "blue-green", "canary",
        "rolling update", "recreate", "shadow", "feature flag",
        "feature toggle", "a/b testing", "multivariate", "experiment",
        "observability", "telemetry", "tracing", "logging", "metrics",
        "alerting", "dashboard", "slo", "sla", "sli", "error budget",
        "toil", "automation", "runbook", "playbook", "sop",
    ],
    "design": [
        "design", "a11y", "accessibility", "ux", "ui", "figma",
        "web design", "typography", "color", "layout", "grid",
        "flexbox", "css", "sass", "less", "tailwind", "bootstrap",
        "material", "chakra", "antd", "shadcn", "radix", "mantine",
        "component", "pattern", "molecule", "organism", "template",
        "page", "view", "screen", "route", "navigation", "menu",
        "sidebar", "header", "footer", "modal", "dialog", "drawer",
        "popover", "tooltip", "toast", "notification", "alert",
        "banner", "card", "list", "table", "form", "input", "button",
        "checkbox", "radio", "select", "dropdown", "toggle", "switch",
        "slider", "progress", "spinner", "skeleton", "avatar",
        "badge", "tag", "chip", "breadcrumb", "pagination", "tabs",
        "accordion", "collapse", "carousel", "gallery", "lightbox",
        "timeline", "stepper", "wizard", "flow", "diagram", "chart",
        "graph", "plot", "map", "calendar", "date picker", "time picker",
        "color picker", "rich text", "markdown editor", "code editor",
        "syntax highlight", "diff", "merge", "conflict", "version",
        "history", "undo", "redo", "clipboard", "drag", "drop",
        "sort", "filter", "search", "autocomplete", "typeahead",
        "command palette", "spotlight", "quick open", "go to",
        "symbol", "definition", "reference", "implementation",
        "rename", "refactor", "extract", "inline", "move", "copy",
        "paste", "cut", "delete", "insert", "replace", "transform",
        "format", "prettify", "minify", "obfuscate", "uglify",
        "compress", "gzip", "brotli", "deflate", "encode", "decode",
        "encrypt", "decrypt", "hash", "sign", "verify", "certificate",
        "tls", "ssl", "https", "http", "websocket", "sse", "grpc",
        "graphql", "rest", "soap", "xml", "json", "yaml", "toml",
        "csv", "tsv", "markdown", "html", "css", "javascript",
        "typescript", "jsx", "tsx", "vue", "svelte", "angular",
        "react", "next.js", "nuxt", "gatsby", "remix", "astro",
        "solid", "qwik", "fresh", "deno", "bun", "node", "npm",
        "yarn", "pnpm", "webpack", "vite", "rollup", "esbuild",
        "turbopack", "turborepo", "nx", "lerna", "monorepo",
    ],
    "research": [
        "academic", "research", "paper", "literature", "arxiv",
        "synthesis", "hypothesis", "experiment", "methodology",
        "peer review", "citation", "bibliography", "doi", "isbn",
        "journal", "conference", "proceedings", "preprint", "postprint",
        "thesis", "dissertation", "abstract", "introduction",
        "background", "related work", "method", "results", "discussion",
        "conclusion", "future work", "acknowledgment", "reference",
        "appendix", "figure", "table", "equation", "theorem", "proof",
        "lemma", "corollary", "proposition", "definition", "axiom",
        "conjecture", "model", "simulation", "analysis", "evaluation",
        "benchmark", "dataset", "corpus", "annotation", "label",
        "ground truth", "baseline", "state of the art", "sota",
        "novel", "contribution", "impact", "significance", "limitation",
        "threat to validity", "reproducibility", "replication",
        "open science", "open data", "open access", "fair", "findable",
        "accessible", "interoperable", "reusable", "metadata", "schema",
        "ontology", "taxonomy", "taxonomy", "classification", "clustering",
        "regression", "classification", "prediction", "forecasting",
        "time series", "signal processing", "image processing",
        "computer vision", "natural language processing", "nlp",
        "large language model", "llm", "transformer", "attention",
        "bert", "gpt", "t5", "llama", "mistral", "claude", "gemini",
        "fine-tuning", "instruction tuning", "rlhf", "dpo", "ppo",
        "reinforcement learning", "supervised learning", "unsupervised",
        "semi-supervised", "self-supervised", "transfer learning",
        "domain adaptation", "few-shot", "zero-shot", "in-context",
        "chain of thought", "cot", "reasoning", "planning", "search",
        "optimization", "gradient", "backpropagation", "loss",
        "objective", "cost", "reward", "policy", "value", "q-learning",
        "actor-critic", "monte carlo", "temporal difference", "td",
        "markov decision process", "mdp", "bandit", "exploration",
        "exploitation", "regret", "sample complexity", "generalization",
        "overfitting", "underfitting", "regularization", "dropout",
        "batch norm", "layer norm", "weight decay", "learning rate",
        "scheduler", "cosine", "warmup", "early stopping", "checkpoint",
        "resume", "distributed", "parallel", "data parallel", "model parallel",
        "pipeline parallel", "tensor parallel", "expert parallel",
        "mixture of experts", "moe", "sparse", "dense", "quantization",
        "pruning", "distillation", "knowledge distillation", "kd",
    ],
    "writing": [
        "writing", "copy", "content", "editorial", "fragments",
        "blog", "article", "essay", "report", "documentation",
        "readme", "changelog", "release note", "announcement",
        "press release", "newsletter", "email", "subject line",
        "headline", "title", "subtitle", "caption", "alt text",
        "meta description", "og tag", "twitter card", "schema.org",
        "structured data", "rich snippet", "featured snippet",
        "seo", "search engine", "keyword", "intent", "long-tail",
        "short-tail", "head term", "question", "how to", "what is",
        "why", "when", "where", "who", "guide", "tutorial", "walkthrough",
        "overview", "introduction", "getting started", "quickstart",
        "faq", "troubleshooting", "debugging", "error", "warning",
        "note", "tip", "best practice", "pattern", "anti-pattern",
        "recipe", "cookbook", "reference", "api reference", "sdk",
        "cli reference", "command reference", "option", "flag",
        "argument", "parameter", "environment variable", "config",
        "configuration", "setting", "preference", "default", "example",
        "sample", "demo", "showcase", "case study", "testimonial",
        "review", "rating", "star", "comparison", "vs", "versus",
        "alternative", "migration", "upgrade", "deprecation",
        "breaking change", "changelog", "release", "version", "semver",
        "calendar versioning", "0.x", "1.x", "alpha", "beta", "rc",
        "preview", "nightly", "canary", "stable", "lts", "long term",
        "support", "maintenance", "end of life", "eol", "deprecated",
        "obsolete", "legacy", "sunset", "retire", "remove", "delete",
    ],
    "media": [
        "image", "video", "audio", "animation", "gif", "svg",
        "png", "jpg", "jpeg", "webp", "avif", "heic", "heif",
        "tiff", "bmp", "ico", "icon", "favicon", "thumbnail",
        "poster", "cover", "banner", "hero", "background", "texture",
        "pattern", "gradient", "overlay", "blend", "filter", "effect",
        "transition", "transform", "scale", "rotate", "translate",
        "skew", "perspective", "3d", "2d", "vector", "raster",
        "pixel", "resolution", "dpi", "ppi", "aspect ratio",
        "frame rate", "fps", "bitrate", "codec", "h264", "h265",
        "vp9", "av1", "aac", "mp3", "ogg", "wav", "flac", "opus",
        "midi", "music", "song", "album", "artist", "genre", "playlist",
        "podcast", "episode", "show", "series", "season", "trailer",
        "clip", "highlight", "recording", "stream", "live", "vod",
        "on demand", "broadcast", "webcast", "webinar", "conference",
        "meetup", "event", "talk", "presentation", "slide", "deck",
        "keynote", "lightning", "panel", "workshop", "tutorial",
        "course", "lesson", "module", "curriculum", "syllabus",
        "certificate", "badge", "credential", "degree", "diploma",
    ],
    "business": [
        "business", "strategy", "growth", "revenue", "profit", "margin",
        "cost", "budget", "forecast", "plan", "roadmap", "milestone",
        "okr", "kpi", "metric", "analytics", "insight", "dashboard",
        "report", "presentation", "stakeholder", "executive", "c-level",
        "ceo", "cto", "cfo", "coo", "cmo", "cio", "vp", "director",
        "manager", "lead", "senior", "junior", "intern", "contractor",
        "freelancer", "consultant", "agency", "vendor", "partner",
        "customer", "client", "user", "buyer", "seller", "merchant",
        "supplier", "distributor", "reseller", "affiliate", "referral",
        "channel", "marketplace", "platform", "ecosystem", "network",
        "community", "audience", "follower", "subscriber", "member",
        "attendee", "participant", "contributor", "maintainer", "owner",
        "founder", "co-founder", "investor", "angel", "seed", "series",
        "a round", "b round", "c round", "ipo", "acquisition", "merger",
        "divestiture", "spin-off", "subsidiary", "joint venture",
        "partnership", "alliance", "collaboration", "sponsorship",
        "donation", "grant", "funding", "crowdfunding", "kickstarter",
        "indiegogo", "patreon", "open source", "license", "copyright",
        "trademark", "patent", "intellectual property", "ip", "nda",
        "non-disclosure", "contract", "agreement", "terms", "conditions",
        "privacy", "policy", "gdpr", "ccpa", "hipaa", "sox", "pci",
        "dss", "iso", "soc2", "compliance", "audit", "certification",
        "accreditation", "standard", "framework", "methodology", "agile",
        "scrum", "kanban", "lean", "six sigma", "total quality", "tqm",
        "continuous improvement", "kaizen", "retrospective", "sprint",
        "iteration", "increment", "backlog", "story", "epic", "task",
        "bug", "defect", "issue", "ticket", "incident", "problem",
        "change", "release", "deploy", "rollback", "hotfix", "patch",
    ],
    "runtime-tools": [
        "runtime", "tool", "utility", "library", "package", "module",
        "framework", "sdk", "cli", "command", "terminal", "shell",
        "script", "automation", "cron", "schedule", "timer", "trigger",
        "event", "listener", "handler", "callback", "hook", "middleware",
        "plugin", "extension", "addon", "integration", "connector",
        "adapter", "driver", "provider", "client", "server", "proxy",
        "gateway", "load balancer", "cache", "queue", "stream", "buffer",
        "pool", "connection", "session", "cookie", "token", "key",
        "secret", "credential", "certificate", "tls", "ssl", "https",
        "http", "websocket", "grpc", "graphql", "rest", "soap", "xml",
        "json", "yaml", "toml", "csv", "tsv", "markdown", "html", "css",
        "javascript", "typescript", "python", "rust", "go", "java",
        "kotlin", "swift", "objective-c", "c\\+\\+", "c#", "f#",
        "ruby", "php", "perl", "lua", "r", "matlab", "scala", "clojure",
        "haskell", "erlang", "elixir", "dart", "flutter", "react",
        "vue", "angular", "svelte", "next.js", "nuxt", "gatsby",
        "remix", "astro", "solid", "qwik", "fresh", "deno", "bun",
        "node", "npm", "yarn", "pnpm", "webpack", "vite", "rollup",
        "esbuild", "turbopack", "turborepo", "nx", "lerna", "monorepo",
    ],
}

HIGH_RISK = [
    # Offensive tooling & techniques (high-confidence indicators)
    "phishing", "malware", "ransomware", "mimikatz", "cobalt strike",
    "keylogger", "rootkit", "backdoor", "trojan", "worm",
    "pass-the-hash", "pass-the-ticket", "kerberoasting", "as-rep roasting",
    "golden ticket", "silver ticket", "diamond ticket", "dcsync", "dcshadow",
    "shadow credentials", "sharpdpapi", "sharpchrome",
    "rubeus", "certipy", "bloodhound",
    "cobalt strike", "covenant", "sliver", "mythic", "havoc",
    "metasploit", "meterpreter", "reverse shell", "bind shell",
    "command and control", "c2", "lateral movement", "data exfiltration",
    "spear phishing", "watering hole",
    "social engineering",
    "dumpster diving", "shoulder surfing",
    "eavesdropping", "stalking", "harassment",
    "doxxing", "swatting", "revenge porn",
]

MEDIUM_RISK = [
    "deploy", "configure", "install", "delete", "migrate",
    "write", "modify", "cloud", "kubernetes", "production",
    "infrastructure", "network", "firewall", "dns", "domain",
    "server", "database", "storage", "backup", "restore",
    "snapshot", "image", "template", "stack", "cluster",
    "node", "pod", "container", "service", "endpoint",
    "api", "gateway", "proxy", "load balancer", "cdn",
    "cdn", "cache", "queue", "stream", "topic", "subscription",
    "function", "lambda", "trigger", "rule", "policy",
    "role", "permission", "access", "identity", "authentication",
    "authorization", "encryption", "decryption", "certificate",
    "key", "secret", "token", "credential", "password",
    "hash", "salt", "nonce", "iv", "mac", "hmac",
    "signature", "verification", "validation", "integrity",
    "audit", "log", "monitor", "alert", "notify", "report",
    "dashboard", "metric", "trace", "span", "event",
    "incident", "response", "remediation", "mitigation",
    "patch", "update", "upgrade", "rollback", "rollback",
    "failover", "disaster recovery", "business continuity",
    "high availability", "scalability", "performance", "reliability",
    "resilience", "fault tolerance", "redundancy", "replication",
    "sharding", "partitioning", "indexing", "caching", "buffering",
    "pooling", "throttling", "rate limiting", "backpressure",
    "circuit breaker", "retry", "timeout", "deadline", "sla",
    "slo", "sli", "error budget", "burn rate", "toil",
]

LOW_RISK = [
    "review", "summarize", "explain", "document", "classify",
    "audit", "analyze", "describe", "list", "enumerate",
    "compare", "contrast", "evaluate", "assess", "measure",
    "benchmark", "profile", "trace", "debug", "inspect",
    "read", "search", "find", "lookup", "query", "filter",
    "sort", "group", "aggregate", "count", "sum", "average",
    "min", "max", "median", "percentile", "distribution",
    "histogram", "scatter", "plot", "chart", "graph",
    "visualize", "display", "render", "format", "print",
    "log", "record", "note", "comment", "annotate", "tag",
    "label", "name", "title", "describe", "define", "declare",
    "import", "export", "include", "extend", "inherit",
    "compose", "combine", "merge", "split", "extract",
    "transform", "convert", "encode", "decode", "serialize",
    "deserialize", "parse", "stringify", "json", "yaml",
    "xml", "csv", "markdown", "html", "text", "binary",
]

# Tag normalization map
TAG_NORMALIZE = {
    "a11y": "accessibility",
    "k8s": "kubernetes",
    "entra-id": "entra-id",
    "azure-ad": "entra-id",
    "agent-skill": "agent-operations",
    "okf": "okf",
    "software-development": "software-engineering",
    "devops": "devops",
    "agent-operations": "agent-operations",
    "security": "security",
    "red-team": "red-team",
    "blue-team": "blue-team",
    "purple-team": "purple-team",
    "threat-intelligence": "threat-intelligence",
    "incident-response": "incident-response",
    "digital-forensics": "digital-forensics",
    "malware-analysis": "malware-analysis",
    "reverse-engineering": "reverse-engineering",
    "vulnerability-management": "vulnerability-management",
    "penetration-testing": "penetration-testing",
    "bug-bounty": "bug-bounty",
    "security-research": "security-research",
    "compliance": "compliance",
    "governance": "governance",
    "risk-management": "risk-management",
    "audit": "audit",
    "logging": "logging",
    "monitoring": "monitoring",
    "observability": "observability",
    "tracing": "tracing",
    "metrics": "metrics",
    "alerting": "alerting",
    "ci-cd": "ci-cd",
    "infrastructure-as-code": "infrastructure-as-code",
    "iac": "infrastructure-as-code",
    "container-security": "container-security",
    "kubernetes-security": "kubernetes-security",
    "cloud-security": "cloud-security",
    "application-security": "application-security",
    "appsec": "application-security",
    "web-security": "web-security",
    "network-security": "network-security",
    "endpoint-security": "endpoint-security",
    "data-security": "data-security",
    "database-security": "database-security",
    "api-security": "api-security",
    "mobile-security": "mobile-security",
    "iot-security": "iot-security",
    "ot-security": "ot-security",
    "ics-security": "ics-security",
    "scada-security": "scada-security",
    "medical-device-security": "medical-device-security",
    "automotive-security": "automotive-security",
    "aerospace-security": "aerospace-security",
    "maritime-security": "maritime-security",
    "satellite-security": "satellite-security",
    "supply-chain-security": "supply-chain-security",
    "open-source-security": "open-source-security",
    "dependency-security": "dependency-security",
    "secrets-management": "secrets-management",
    "identity-access-management": "identity-access-management",
    "iam": "identity-access-management",
    "privileged-access-management": "privileged-access-management",
    "pam": "privileged-access-management",
    "zero-trust": "zero-trust",
    "ztna": "zero-trust-network-access",
    "sase": "secure-access-service-edge",
    "sse": "security-service-edge",
    "casb": "cloud-access-security-broker",
    "cspm": "cloud-security-posture-management",
    "cwpp": "cloud-workload-protection-platform",
    "cnapp": "cloud-native-application-protection-platform",
    "aspm": "application-security-posture-management",
    "vm": "vulnerability-management",
    "pt": "penetration-testing",
    "ir": "incident-response",
    "dfir": "digital-forensics-incident-response",
    "cti": "cyber-threat-intelligence",
    "soc": "security-operations-center",
    "noc": "network-operations-center",
    "mssp": "managed-security-service-provider",
    "mdr": "managed-detection-response",
    "xdr": "extended-detection-response",
    "ndr": "network-detection-response",
    "edr": "endpoint-detection-response",
    "mdm": "mobile-device-management",
    "mam": "mobile-application-management",
    "uem": "unified-endpoint-management",
    "dlp": "data-loss-prevention",
    "iam": "identity-access-management",
    "pim": "privileged-identity-management",
    "pam": "privileged-access-management",
    "sso": "single-sign-on",
    "mfa": "multi-factor-authentication",
    "2fa": "two-factor-authentication",
    "fido2": "fido2",
    "webauthn": "webauthn",
    "oauth": "oauth",
    "oidc": "openid-connect",
    "saml": "saml",
    "ldap": "ldap",
    "ad": "active-directory",
    "entra": "microsoft-entra-id",
    "azure-ad": "microsoft-entra-id",
    "gcp": "google-cloud-platform",
    "aws": "amazon-web-services",
    "azure": "microsoft-azure",
    "oci": "oracle-cloud-infrastructure",
    "ibm-cloud": "ibm-cloud",
    "alibaba-cloud": "alibaba-cloud",
    "tencent-cloud": "tencent-cloud",
    "digitalocean": "digitalocean",
    "linode": "linode",
    "vultr": "vultr",
    "heroku": "heroku",
    "vercel": "vercel",
    "netlify": "netlify",
    "cloudflare": "cloudflare",
    "fastly": "fastly",
    "akamai": "akamai",
    "aws-lambda": "aws-lambda",
    "azure-functions": "azure-functions",
    "gcp-cloud-functions": "gcp-cloud-functions",
    "kubernetes": "kubernetes",
    "k8s": "kubernetes",
    "docker": "docker",
    "podman": "podman",
    "containerd": "containerd",
    "cri-o": "cri-o",
    "openshift": "openshift",
    "rancher": "rancher",
    "eks": "amazon-eks",
    "aks": "azure-kubernetes-service",
    "gke": "google-kubernetes-engine",
    "terraform": "terraform",
    "pulumi": "pulumi",
    "ansible": "ansible",
    "chef": "chef",
    "puppet": "puppet",
    "saltstack": "saltstack",
    "cloudformation": "aws-cloudformation",
    "cdk": "aws-cdk",
    "arm-template": "azure-resource-manager-template",
    "bicep": "azure-bicep",
    "deployment-manager": "gcp-deployment-manager",
    "crossplane": "crossplane",
    "helm": "helm",
    "kustomize": "kustomize",
    "flux": "flux",
    "argo-cd": "argo-cd",
    "spinnaker": "spinnaker",
    "jenkins": "jenkins",
    "github-actions": "github-actions",
    "gitlab-ci": "gitlab-ci",
    "circleci": "circleci",
    "travis-ci": "travis-ci",
    "azure-devops": "azure-devops",
    "teamcity": "teamcity",
    "bamboo": "bamboo",
    "drone": "drone",
    "tekton": "tekton",
    "buildkite": "buildkite",
    "codefresh": "codefresh",
    "harness": "harness",
    "spacelift": "spacelift",
    "env0": "env0",
    "scalr": "scalr",
    "terragrunt": "terragrunt",
    "atmos": "atmos",
    "brainboard": "brainboard",
    "iac": "infrastructure-as-code",
    "gitops": "gitops",
    "devops": "devops",
    "devsecops": "devsecops",
    "sre": "site-reliability-engineering",
    "platform-engineering": "platform-engineering",
    "developer-experience": "developer-experience",
    "dx": "developer-experience",
    "productivity": "productivity",
    "efficiency": "efficiency",
    "automation": "automation",
    "scripting": "scripting",
    "bash": "bash",
    "shell": "shell",
    "powershell": "powershell",
    "python": "python",
    "javascript": "javascript",
    "typescript": "typescript",
    "java": "java",
    "kotlin": "kotlin",
    "swift": "swift",
    "objective-c": "objective-c",
    "c\\+\\+": "cpp",
    "c#": "csharp",
    "f#": "fsharp",
    "go": "go",
    "rust": "rust",
    "ruby": "ruby",
    "php": "php",
    "perl": "perl",
    "lua": "lua",
    "r": "r",
    "matlab": "matlab",
    "scala": "scala",
    "clojure": "clojure",
    "haskell": "haskell",
    "erlang": "erlang",
    "elixir": "elixir",
    "dart": "dart",
    "flutter": "flutter",
    "react": "react",
    "vue": "vue",
    "angular": "angular",
    "svelte": "svelte",
    "next.js": "nextjs",
    "nuxt": "nuxt",
    "gatsby": "gatsby",
    "remix": "remix",
    "astro": "astro",
    "solid": "solid-js",
    "qwik": "qwik",
    "fresh": "fresh",
    "deno": "deno",
    "bun": "bun",
    "node": "nodejs",
    "express": "express",
    "fastify": "fastify",
    "koa": "koa",
    "hapi": "hapi",
    "nest": "nestjs",
    "django": "django",
    "flask": "flask",
    "fastapi": "fastapi",
    "spring": "spring-boot",
    "rails": "ruby-on-rails",
    "laravel": "laravel",
    "symfony": "symfony",
    "yii": "yii",
    "cakephp": "cakephp",
    "codeigniter": "codeigniter",
    "slim": "slim",
    "sinatra": "sinatra",
    "hanami": "hanami",
    "roda": "roda",
    "cuba": "cuba",
    "grape": "grape",
    "roar": "roar",
}

# Source fingerprint patterns
SOURCE_FINGERPRINTS = {
    "anthropic-cybersecurity-skills": [
        "mitre att&ck", "mitre att&ck", "att&ck", "t1", "t15", "t16",
        "ghostpack", "mimikatz", "cobalt strike", "bloodhound", "rubeus",
        "impacket", "crackmapexec", "certipy", "pywhisker", "whisker",
        "sharpdpapi", "sharpchrome", "evil-winrm", "metasploit",
    ],
    "matt-pocock-skills": [
        "matt pocock", "matt-pocock", "@mattpocockuk",
    ],
    "addy-osmani-skills": [
        "addy osmani", "addy-osmani", "@addyosmani",
    ],
    "vercel-skills": [
        "vercel", "next.js", "nextjs", "swr", "turbo", "v0",
    ],
    "agent-skills-standard": [
        "agent skills", "agent-skills", "okf", "open knowledge framework",
    ],
    "amok-native": [
        "amok", "agent-memory-ops-kit", "teleagent",
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalize_tag(tag) -> str:
    """Normalize a single tag string."""
    if not isinstance(tag, str):
        tag = str(tag)
    t = tag.strip().lower().replace(" ", "-")
    return TAG_NORMALIZE.get(t, t)


def dedupe_tags(tags) -> list:
    """Deduplicate and normalize tags, preserving first-seen order."""
    seen = set()
    result = []
    if not isinstance(tags, list):
        return result
    for t in tags:
        norm = normalize_tag(t)
        if norm and norm not in seen:
            seen.add(norm)
            result.append(norm)
    return result


# Performance: build a single combined regex per domain for fast matching
DOMAIN_COMBINED = {}
for _domain, _keywords in DOMAIN_RULES.items():
    escaped = [re.escape(kw) for kw in _keywords]
    DOMAIN_COMBINED[_domain] = re.compile(
        r'\b(?:' + '|'.join(escaped) + r')\b', re.IGNORECASE
    )

HIGH_RISK_COMBINED = re.compile(
    r'\b(?:' + '|'.join(re.escape(kw) for kw in HIGH_RISK) + r')\b', re.IGNORECASE
)
MEDIUM_RISK_COMBINED = re.compile(
    r'\b(?:' + '|'.join(re.escape(kw) for kw in MEDIUM_RISK) + r')\b', re.IGNORECASE
)
LOW_RISK_COMBINED = re.compile(
    r'\b(?:' + '|'.join(re.escape(kw) for kw in LOW_RISK) + r')\b', re.IGNORECASE
)


def derive_domain(text: str, tags: list, name: str) -> tuple[str, float]:
    """Return (domain, confidence). Uses single combined regex per domain for speed."""
    haystack = (text + " " + " ".join(tags) + " " + name).lower()
    scores = Counter()
    for domain, pattern in DOMAIN_COMBINED.items():
        matches = pattern.findall(haystack)
        if matches:
            scores[domain] = len(matches)
    if not scores:
        return "uncategorized", 0.0
    top, top_score = scores.most_common(1)[0]
    total = sum(scores.values())
    confidence = round(top_score / total, 2) if total else 0.0
    # Apply specificity bonus: more specific domains get a boost
    specificity = {
        "forensics": 1.5, "cloud-security": 1.4, "security-offensive": 1.3,
        "security-defensive": 1.2, "software-engineering": 1.0,
        "agent-operations": 1.1, "research": 1.1, "design": 1.1,
        "business": 1.0, "media": 1.0, "writing": 1.0, "runtime-tools": 0.9,
        "uncategorized": 0.0,
    }
    # Recalculate with specificity
    weighted_scores = {d: s * specificity.get(d, 1.0) for d, s in scores.items()}
    top = max(weighted_scores, key=weighted_scores.get)
    total_w = sum(weighted_scores.values())
    confidence = round(weighted_scores[top] / total_w, 2) if total_w else 0.0
    return top, confidence


def derive_risk(text: str, tags: list, name: str) -> tuple[str, bool, list[str]]:
    """Return (risk_level, requires_review, reasons). Uses single combined regex for speed."""
    haystack = (text + " " + " ".join(tags) + " " + name).lower()
    reasons = []

    high_matches = HIGH_RISK_COMBINED.findall(haystack)
    med_matches = MEDIUM_RISK_COMBINED.findall(haystack)
    low_matches = LOW_RISK_COMBINED.findall(haystack)

    if high_matches:
        risk = "high"
        requires_review = True
        # Deduplicate and get unique high hits
        unique_high = list(dict.fromkeys(high_matches))
        reasons = [f"high-risk: {h}" for h in unique_high[:5]]
    elif med_matches:
        risk = "medium"
        unique_med = list(dict.fromkeys(med_matches))
        requires_review = len(unique_med) >= 3
        reasons = [f"medium-risk: {h}" for h in unique_med[:5]]
    elif low_matches:
        risk = "low"
        requires_review = False
        reasons = []
    else:
        risk = "low"
        requires_review = False
        reasons = []

    return risk, requires_review, reasons


def fingerprint_source(text: str, tags: list) -> tuple[str, float]:
    """Return (source_family, confidence)."""
    haystack = (text + " " + " ".join(tags)).lower()
    scores = Counter()
    for family, patterns in SOURCE_FINGERPRINTS.items():
        for pat in patterns:
            if pat in haystack:
                scores[family] += 1
    if not scores:
        return "unknown", 0.0
    top, top_score = scores.most_common(1)[0]
    confidence = round(top_score / len(SOURCE_FINGERPRINTS[top]), 2)
    return top, min(confidence, 1.0)


def quality_gate_check(fm: dict, body: str, name: str, risk: str, requires_review: bool, domain: str) -> list[str]:
    """Return list of quality issues (empty = clean)."""
    issues = []
    if not fm:
        issues.append("missing frontmatter")
    if not fm.get("type"):
        issues.append("missing type")
    if not fm.get("name") and not fm.get("title"):
        issues.append("missing name/title")
    desc = fm.get("description", "")
    if not desc or (isinstance(desc, str) and len(desc.strip()) < 20):
        issues.append("description too short")
    if isinstance(desc, str) and desc.strip() == ">-":
        issues.append("broken folded description")
    body_stripped = body.strip()
    if len(body_stripped) < 100:
        issues.append("body too short (<100 chars)")
    if risk == "high" and not requires_review:
        issues.append("high-risk without requires_review=true")
    # Only flag missing safety framing for offensive domains
    if risk == "high" and domain in ("security-offensive",) and "legal" not in body_stripped.lower() and "authorized" not in body_stripped.lower():
        issues.append("high-risk offensive without safety/legal framing")
    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    files = sorted(ROOT.rglob("*.md"))
    rows = []
    domain_counter = Counter()
    risk_counter = Counter()
    source_counter = Counter()
    quality_flagged = []
    type_counter = Counter()

    for path in files:
        rel = path.relative_to(ROOT)
        name = rel.parts[0] if len(rel.parts) > 1 else path.stem
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)

        raw_tags = fm.get("tags", [])
        if not isinstance(raw_tags, list):
            raw_tags = [str(raw_tags)]
        tags = dedupe_tags(raw_tags)

        heading = first_heading(body)
        title = (
            str(fm.get("title", "")).strip()
            or heading
            or str(fm.get("name", "")).strip()
            or slug_to_title(name)
        )
        typ = str(fm.get("type", "")).strip()
        desc = str(fm.get("description", "")).strip()
        if not desc:
            desc = first_meaningful_paragraph(body)

        domain, domain_conf = derive_domain(text, tags, name)
        risk, requires_review, risk_reasons = derive_risk(text, tags, name)
        source_family, source_conf = fingerprint_source(text, tags)
        tags = normalize_tags(tags, domain)
        issues = quality_gate_check(fm, body, name, risk, requires_review, domain)

        domain_counter[domain] += 1
        risk_counter[risk] += 1
        source_counter[source_family] += 1
        type_counter[typ or "_missing"] += 1

        if issues:
            quality_flagged.append({
                "path": str(rel),
                "name": name,
                "issues": issues,
            })

        rows.append({
            "path": str(rel),
            "name": name,
            "title": title,
            "type": typ,
            "description": desc,
            "tags": tags,
            "domain": domain,
            "domain_confidence": domain_conf,
            "risk_level": risk,
            "requires_review": requires_review,
            "risk_reasons": risk_reasons,
            "source_family": source_family,
            "source_confidence": source_conf,
            "quality_issues": issues,
            "source_status": fm.get("source_status", ""),
            "source_name": fm.get("source_name", ""),
            "source_url": fm.get("source_url", ""),
            "source_license": fm.get("source_license", ""),
            "license": fm.get("license", ""),
        })

    # Write enriched inventory
    (OUT / "dist-skills-enriched-inventory.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Write frontmatter proposals
    proposals = []
    for r in rows:
        proposal = {
            "path": r["path"],
            "proposed_frontmatter": {
                "name": r["name"],
                "title": r["title"],
                "description": r["description"],
                "type": r["type"] or "Playbook",
                "tags": r["tags"],
                "domain": r["domain"],
                "risk_level": r["risk_level"],
                "requires_review": r["requires_review"],
                "source_family": r["source_family"],
            },
            "current_frontmatter": {
                "type": r["type"],
                "tags": r["tags"],
                "source_status": r["source_status"],
                "risk_level": r["risk_level"],
                "requires_review": r["requires_review"],
            },
        }
        proposals.append(proposal)

    (OUT / "frontmatter-proposals.json").write_text(
        json.dumps(proposals, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Write quality gate flagged
    (OUT / "quality-gate-flagged.json").write_text(
        json.dumps(quality_flagged, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # --- Markdown reports ---

    def md_counter(title: str, counter: Counter, limit=None) -> str:
        items = counter.most_common(limit)
        lines = [f"## {title}", "", "| Value | Count |", "|---|---:|"]
        for key, count in items:
            lines.append(f"| `{key}` | {count} |")
        return "\n".join(lines)

    # Domain report
    domain_report = [
        "# dist/skills Domain Report",
        "",
        f"Total skills: **{len(files)}**",
        "",
        md_counter("By derived domain", domain_counter),
        "",
        md_counter("By type", type_counter),
        "",
        "### Domain confidence distribution",
        "",
        "| Confidence | Count |",
        "|---|---:|",
    ]
    conf_buckets = Counter()
    for r in rows:
        c = r["domain_confidence"]
        if c >= 0.7:
            conf_buckets["high (>=0.7)"] += 1
        elif c >= 0.4:
            conf_buckets["medium (0.4-0.7)"] += 1
        else:
            conf_buckets["low (<0.4)"] += 1
    for bucket, count in conf_buckets.most_common():
        domain_report.append(f"| {bucket} | {count} |")

    (OUT / "dist-skills-domain-report.md").write_text(
        "\n".join(domain_report), encoding="utf-8"
    )

    # Risk report
    risk_report = [
        "# dist/skills Risk Report",
        "",
        f"Total skills: **{len(files)}**",
        "",
        md_counter("By risk level", risk_counter),
        "",
        "### High-risk skills",
        "",
        "| Path | Risk | Reasons |",
        "|---|---|---|",
    ]
    for r in rows:
        if r["risk_level"] == "high":
            reasons = "; ".join(r["risk_reasons"][:3])
            risk_report.append(f"| `{r['path']}` | {r['risk_level']} | {reasons} |")

    risk_report += [
        "",
        "### Medium-risk skills (sample of 30)",
        "",
        "| Path | Risk | Reasons |",
        "|---|---|---|",
    ]
    medium_shown = 0
    for r in rows:
        if r["risk_level"] == "medium" and medium_shown < 30:
            reasons = "; ".join(r["risk_reasons"][:3])
            risk_report.append(f"| `{r['path']}` | {r['risk_level']} | {reasons} |")
            medium_shown += 1

    risk_report += [
        "",
        "### Skills requiring review",
        "",
        f"Count: **{sum(1 for r in rows if r['requires_review'])}**",
    ]

    (OUT / "dist-skills-risk-report.md").write_text(
        "\n".join(risk_report), encoding="utf-8"
    )

    # Source fingerprint report
    source_report = [
        "# dist/skills Source Fingerprint Report",
        "",
        f"Total skills: **{len(files)}**",
        "",
        md_counter("By inferred source family", source_counter),
        "",
        "### Source confidence distribution",
        "",
        "| Confidence | Count |",
        "|---|---:|",
    ]
    src_conf = Counter()
    for r in rows:
        c = r["source_confidence"]
        if c >= 0.5:
            src_conf["high (>=0.5)"] += 1
        elif c >= 0.2:
            src_conf["medium (0.2-0.5)"] += 1
        else:
            src_conf["low (<0.2)"] += 1
    for bucket, count in src_conf.most_common():
        source_report.append(f"| {bucket} | {count} |")

    (OUT / "source-fingerprint.md").write_text(
        "\n".join(source_report), encoding="utf-8"
    )

    # Frontmatter proposals summary
    proposals_summary = [
        "# Frontmatter Proposals Summary",
        "",
        f"Total proposals: **{len(proposals)}**",
        "",
        "This file is proposal-only. No files have been modified.",
        "",
        "## Fields proposed",
        "",
        "- `name`",
        "- `title`",
        "- `description`",
        "- `type`",
        "- `tags` (deduplicated, normalized)",
        "- `domain` (derived)",
        "- `risk_level` (derived)",
        "- `requires_review` (derived)",
        "- `source_family` (inferred)",
        "",
        "## Next steps",
        "",
        "1. Review this report",
        "2. Approve or adjust proposals",
        "3. Run apply_frontmatter_patches.py (not yet written)",
        "",
        "## Sample proposals (first 20)",
        "",
        "```json",
    ]
    for p in proposals[:20]:
        proposals_summary.append(json.dumps(p, indent=2, ensure_ascii=False))
        proposals_summary.append("---")
    proposals_summary.append("```")

    (OUT / "frontmatter-proposals.md").write_text(
        "\n".join(proposals_summary), encoding="utf-8"
    )

    # Print summary
    print(f"Total skills processed: {len(files)}")
    print()
    print("Domain distribution:")
    for domain, count in domain_counter.most_common():
        print(f"  {domain:30s} {count:5d}")
    print()
    print("Risk distribution:")
    for risk, count in risk_counter.most_common():
        print(f"  {risk:15s} {count:5d}")
    print()
    print(f"Quality-flagged: {len(quality_flagged)}")
    print()
    print("Source families:")
    for src, count in source_counter.most_common():
        print(f"  {src:40s} {count:5d}")
    print()
    print("Wrote:")
    print("  reports/dist-skills-enriched-inventory.json")
    print("  reports/dist-skills-domain-report.md")
    print("  reports/dist-skills-risk-report.md")
    print("  reports/frontmatter-proposals.json")
    print("  reports/frontmatter-proposals.md")
    print("  reports/quality-gate-flagged.json")
    print("  reports/source-fingerprint.md")


if __name__ == "__main__":
    main()
