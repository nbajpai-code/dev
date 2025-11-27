# Automation Scripts

This directory contains automation scripts for keeping the repository updated.

## update_content.py

Daily update script that runs via GitHub Actions to:
- Update the "Last Updated" timestamp in README.md
- Check for upcoming events
- Maintain repository freshness

### Manual Execution

```bash
# Install dependencies
pip install requests python-dateutil pytz

# Run the script
python scripts/update_content.py
```

### GitHub Actions

The script runs automatically daily at 12:00 UTC via the `.github/workflows/daily-update.yml` workflow.

## How It Works

1. **Daily Schedule**: Runs every day at 12 PM UTC (7 AM EST / 4 AM PST)
2. **Updates**: Modifies README.md with current date
3. **Auto-commit**: Commits changes directly to main branch (no PRs)
4. **Smart Detection**: Only commits if there are actual changes

## Customization

To modify the update schedule, edit `.github/workflows/daily-update.yml`:

```yaml
on:
  schedule:
    - cron: '0 12 * * *'  # Change this cron expression
```

Common cron schedules:
- `0 12 * * *` - Daily at 12 PM UTC
- `0 */6 * * *` - Every 6 hours
- `0 0 * * 1` - Weekly on Mondays at midnight
- `0 0 1 * *` - Monthly on the 1st at midnight
