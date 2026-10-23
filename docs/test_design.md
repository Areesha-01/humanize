
## Module 3: humanize.time (Areeba)

### naturaldelta(value)
| Technique | Class / Boundary | Input | Expected |
|---|---|---|---|
| ECP | seconds range | 30 seconds | "30 seconds" |
| ECP | hours range | 2 hours | "2 hours" |
| ECP | days / years | 2 days, 365 days | "2 days", "a year" |
| ECP | negative delta | -120 seconds | "2 minutes" (absolute value) |
| ECP | plain number | 45 | "45 seconds" |
| ECP | invalid string | "abc" | "abc" (returned as is) |
| BVA | zero | 0 seconds | "a moment" |
| BVA | one second | 1 second | "a second" |
| BVA | just below a minute | 59 seconds | "59 seconds" |
| BVA | exactly a minute | 60 seconds | "a minute" |
| BVA | exactly an hour / day | 3600 / 86400 seconds | "an hour" / "a day" |
| BVA | minimum_unit | 500 ms, minimum_unit="milliseconds" | "500 milliseconds" |

### naturaltime(value, when=None)
| Technique | Class / Boundary | Input | Expected |
|---|---|---|---|
| ECP | past | timedelta 30 s | "30 seconds ago" |
| ECP | future | timedelta -30 s | "30 seconds from now" |
| ECP | datetime with `when` (past) | 12:00 vs when 12:05 | "5 minutes ago" |
| ECP | datetime with `when` (future) | 12:10 vs when 12:05 | "5 minutes from now" |
| ECP | invalid string | "abc" | "abc" |
| BVA | zero difference | 0 seconds | "now" |
| BVA | 1 s, 60 s, 3600 s, 86400 s | past and future | "a second ago", "a minute ago", "an hour ago", "a day ago" (and "from now") |

## Module 2 (extra, Areeba): humanize.filesize.naturalsize
| Technique | Class / Boundary | Input | Expected |
|---|---|---|---|
| BVA | unit boundaries | 1e6, 1e9, 1e12, 1e15 | "1.0 MB", "1.0 GB", "1.0 TB", "1.0 PB" |
| ECP | rounding | 1234567890 | "1.2 GB" |
| ECP | float input | 1536.5 | "1.5 kB" |
| ECP | numeric string | "2000" | "2.0 kB" |
| ECP | custom format | 1500, format="%.3f" | "1.500 kB" |
| ECP | invalid string | "abc" | raises ValueError |
| ECP | binary large | 1e9, 1e12 | "953.7 MiB", "931.3 GiB" |
| ECP | gnu style | 1024, 1536 | "1.0K", "1.5K" |
