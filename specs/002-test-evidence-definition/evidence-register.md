# Evidence Register

## Evidence Register Entries

| Claim | Classification | Source or decision reference | Provenance | Review status |
|---|---|---|---|---|
| Persistence reading status is `UNAVAILABLE`: no table or field was recorded because the instrument had no view of persistence; this is a limit of the reading, not a finding that the estate stores nothing. | documented reading limit | [data_model.md](../../../../old/docs/data_model.md) — `UNAVAILABLE` | Legacy reading | supported |
| Endpoint reading status is `UNAVAILABLE`: no endpoint was recorded; the reading does not determine whether the estate exposes none or whether its routing was unrecognised. | documented reading limit | [api_surface.md](../../../../old/docs/api_surface.md) — `UNAVAILABLE` | Legacy reading | supported |
| Security reading status is `Could not search`: the code graph could not be searched, so no security evidence was looked for. | documented reading limit | [security.md](../../../../old/docs/security.md) — `Could not search` | Legacy reading | supported |
| Edge-case reading status is `Could not search`: the code graph could not be searched, so no edge-case evidence was looked for. | documented reading limit | [edge_cases.md](../../../../old/docs/edge_cases.md) — `Could not search` | Legacy reading | supported |
| Workflow reading status is `Could not search`: the code graph could not be searched, so no workflow evidence was looked for. | documented reading limit | [workflows.md](../../../../old/docs/workflows.md) — `Could not search` | Legacy reading | supported |

## Allowed Classification Values

- `verified legacy evidence`
- `documented reading limit`
- `supported inference`
- `proposed scope decision`

## Allowed Review Status Values

- `supported`
- `unresolved`
- `blocked`
- `rejected`
