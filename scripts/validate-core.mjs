import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const manifest = JSON.parse(fs.readFileSync(path.join(root, "core/manifest.json"), "utf8"));
const errors = [];
for (const slug of manifest.skills || []) {
  const file = path.join(root, "core/skills", `${slug}.md`);
  if (!fs.existsSync(file)) { errors.push(`missing core skill ${slug}`); continue; }
  const text = fs.readFileSync(file, "utf8");
  for (const field of ["type: Skill", "title:", "description:", "source_status:", "source_name:", "source_license:", "risk_level:", "requires_review:", "## Trigger", "## Inputs", "## Procedure", "## Verification", "## Failure Modes"]) {
    if (!text.includes(field)) errors.push(`${slug} missing ${field}`);
  }
}
if (errors.length) { console.error(errors.join("\n")); process.exit(1); }
console.log(`reviewed core validation passed (${manifest.skills.length} skills)`);
