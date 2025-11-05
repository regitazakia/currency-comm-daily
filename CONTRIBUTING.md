# Contributing to Development Economics Monitor

Thank you for your interest in contributing! This project aims to make development economics data more accessible to researchers, policymakers, and anyone interested in global development.

## Ways to Contribute

### 1. Add New Data Sources

We're always looking for additional reliable, free data sources. Good additions:
- Daily-updated economic indicators
- Development-relevant metrics
- Data from authoritative sources (World Bank, UN, IMF, regional development banks)

**To add a data source:**
1. Create a new fetcher script in `scripts/`
2. Follow the pattern of existing scripts
3. Save data in appropriate format (CSV + JSON)
4. Update the GitHub Actions workflow
5. Document in README.md

### 2. Improve Data Collection Scripts

- Better error handling
- More robust API calls
- Data validation
- Retry logic for failed requests

### 3. Add Analysis Features

- Statistical summaries
- Trend detection
- Anomaly identification
- Visualization generation
- Export to common formats

### 4. Enhance Documentation

- Add usage examples
- Create tutorials
- Document data structure
- Add research use cases
- Improve comments in code

### 5. Fix Bugs

Check the Issues tab for known bugs or report new ones.

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/dev-economics-monitor.git
cd dev-economics-monitor

# Install dependencies
pip install -r requirements.txt

# Test scripts locally
python scripts/fetch_currency_rates.py
python scripts/generate_summary.py
```

## Code Guidelines

### Python Scripts

- Use Python 3.8+
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Include error handling
- Print informative status messages
- Use type hints where appropriate

### Data Storage

- Save data in both CSV and JSON formats
- Use ISO date format: YYYY-MM-DD
- Include timestamps in ISO 8601 format
- Maintain backwards compatibility

### GitHub Actions

- Keep workflows efficient
- Use appropriate failure handling
- Add descriptive step names
- Include helpful output messages

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your fork (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### PR Checklist

- [ ] Code follows project style
- [ ] Scripts tested locally
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
- [ ] Commit messages are clear

## Data Source Criteria

New data sources should be:
- **Reliable**: From authoritative institutions
- **Free**: Publicly accessible without cost
- **Relevant**: Related to development economics
- **Updated**: Regularly maintained
- **Documented**: Clear methodology and definitions

## Ideas for Contributions

### High Priority
- Automated FAO Food Price Index scraping
- World Bank commodity price API integration
- Data visualization dashboard
- Jupyter notebook with analysis examples

### Medium Priority
- Additional currency pairs
- Regional development banks data
- Climate/environmental indicators
- Health and education metrics

### Nice to Have
- Web interface for data exploration
- API for accessing collected data
- Automated report generation
- Email/SMS alerts for significant changes

## Questions?

Open an issue for:
- Feature requests
- Bug reports
- Questions about the code
- Discussion of new data sources
- Help with setup

## Code of Conduct

Be respectful, constructive, and collaborative. This project aims to support global development research and policy - let's keep that mission front and center.

## Recognition

Contributors will be recognized in:
- README.md acknowledgments
- Release notes
- Project documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Together, we're making development economics data more accessible! 🌍**
