# UI Design Usage

## Use this Skill for

- designing one concrete page or flow before source implementation;
- producing wireframes, high-fidelity views, interaction/state specifications, or a bounded UI prototype;
- comparing supplied or generated UI alternatives against verified product facts;
- preparing a complete `dev-frontend` handoff for the selected surface;
- changing shared tokens, component semantics, variants, or overall visual language through the conditional Design System profile;
- extracting or maintaining an accepted shared design package without editing product source.

Using existing shared components does not by itself activate the Design System profile. A normal page or flow stays in Feature UI and references the current owners.

## Typical Chain

```text
product facts -> ui-design (Feature UI by default) -> dev-frontend
                         -> host image tool when needed
                         -> ops-browser or ops-client
                         -> audit-frontend -> repo-review -> repo-delivery
```

Start with `product-spec` only when behavior, permissions, failure semantics, or acceptance remain unresolved. A clear UI request can start directly with `ui-design`; ordinary implementation does not require `repo-map` first.

## Artifact Locations

Prefer repository-defined locations. Otherwise keep durable shared-system facts under `docs/ui/` and task-local Feature UI evidence under `artifacts/ui/<task-id>/`. A Feature UI task should not create a shared manifest or rewrite the accepted profile unless it actually changes shared ownership.

## Handoff Examples

- `dev-frontend`: target route/surface, evidence revision, chosen direction, layouts, exact states and transitions, current tokens/components to reuse, shared changes if any, responsive/accessibility rules, copy, assets, hard blockers, and acceptance checks.
- Host image tool: constrained subject, composition, content facts, explicit exclusions, aspect/size, reference `use`/`ignore`, and finite variant budget. Returned images remain design evidence.
- `ops-browser`: target URL, viewport/state matrix, exact assertions, console/network expectations, and screenshot paths.
- `ops-client`: launch command, expected app/window identity, target size, fixture, assertions, and screenshot path.

## Output Boundary

Wireframes, mockups, generated images, and prototypes prove a design option only. They do not prove source implementation, browser behavior, native-window behavior, accessibility, network behavior, or deployment.
