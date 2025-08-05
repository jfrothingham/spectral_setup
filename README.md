# Spectral Setup

A Python toolkit for visualizing and analyzing radio telescope receiver frequency ranges, specifically designed for Green Bank Observatory (GBO) receivers.

## Overview

This project provides tools to:
- Load and parse receiver frequency data from CSV files
- Create frequency range dictionaries for easy programmatic access
- Generate plots showing receiver frequency coverage
- Support future integration with VEGAS observing modes

## Files

### Core Scripts

- **`freqsetup.py`** - Loads receiver data from CSV and creates a frequency dictionary
- **`spectralplotter.py`** - Main plotting script for visualizing receiver frequency ranges
- **`receivers.csv`** - Database of GBT receiver specifications

### Data Structure

The receiver data includes:
- Receiver name
- Minimum/maximum frequency (GHz)
- Focus type (Prime/Gregorian)
- Polarization capabilities
- Number of beams

## Requirements

```python
matplotlib
astropy
numpy
```

## Usage

### Basic Frequency Dictionary Creation

```python
# Run freqsetup.py to create frequency dictionary
python freqsetup.py
```

This creates a `spec_dict_GHz` dictionary with receiver frequency ranges.

### Plotting Receiver Ranges

```python
# Run spectralplotter.py to generate frequency coverage plots
python spectralplotter.py
```

The plotting script:
- Creates logarithmic frequency plots
- Shows frequency ranges as vertical lines with labels
- Currently plots a subset of receivers (Rcvr1_2, Rcvr2_3, Rcvr4_6)
- Can be easily modified to plot all available receivers

### Customizing Plots

To plot different receivers, modify the `toplot` list in `spectralplotter.py`:

```python
# Plot specific receivers
toplot = ['Rcvr1_2', 'Rcvr2_3', 'Rcvr4_6']

# Or plot all receivers
toplot = rcvr_range_ghz_dict.keys()
```

## Receiver Database

The `receivers.csv` file contains data for 14 GBT receivers covering:
- **Low frequencies**: 0.29 - 2.6 GHz (Prime Focus and L-band systems)
- **Mid frequencies**: 3.95 - 40 GHz (C, X, Ku, K, Ka bands)
- **High frequencies**: 40 - 116 GHz (Q, W bands and arrays)

### Sample Receivers

| Receiver | Freq Range (GHz) | Focus | Polarization | Beams |
|----------|------------------|-------|--------------|-------|
| RcvrPF_1 | 0.29 - 0.92 | Prime | linear/circular | 1 |
| Rcvr1_2 | 1.15 - 1.73 | Gregorian | linear/circular | 1 |
| RcvrArray75_115 | 75.0 - 116.0 | Gregorian | linear | 16 |

## Data Source

Receiver data downloaded from the internal GBO tool: https://alda.gb.nrao.edu/receiver/receivers

## Future Development

- Integration with VEGAS mode specifications from GBT Proposer's and Observer's Guides
- Enhanced plotting capabilities
- Spectral line overlays
- Observing session planning tools

## Author

Created by jfrothin on August 4, 2025

## License

This project is intended for use with Green Bank Observatory data and tools.
