#!/usr/bin/env node

const args = process.argv.slice(2);

if (args.includes("--help") || args.includes("-h")) {
  console.log(`architectonic-skills

Runtime-neutral skills bundle for human-agent collaboration.

Usage:
  npx architectonic-skills
  npx architectonic-skills help

This package ships the skills catalog, install manifest, and canonical
dist/skills bundle.`);
  process.exit(0);
}

console.log("architectonic-skills");
console.log("");
console.log("Skill bundle for reusable procedures, install manifests, and progressive discovery.");
console.log("See dist/catalog.json and README.md in the package contents.");
