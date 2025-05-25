# Quantum Key Distribution (QKD) - BB84 Protocol Simulation

A comprehensive Python implementation of the BB84 quantum key distribution protocol for educational purposes, demonstrating how quantum mechanics enables secure key exchange.

## Interactive Infographic

![BB84 Interactive Infographic](bb84/screen.png)

An interactive web-based infographic that provides a comprehensive visual explanation of the BB84 protocol and quantum cryptography principles.

### Accessing the Interactive Infographic:

1. Navigate to the `bb84/` directory
2. Open the `index.html` file in your web browser
3. Explore the interactive demonstration of the BB84 protocol

The infographic features:

- Step-by-step explanation of the BB84 protocol
- Interactive simulations with real-time execution
- Demonstration of eavesdropping detection mechanisms (Eve)
- Real-world applications of quantum cryptography
- Modern, user-friendly interface with educational content

## Overview

This project simulates the BB84 protocol, the first quantum cryptography protocol developed by Bennett and Brassard in 1984. It demonstrates how Alice and Bob can establish a shared secret key while detecting eavesdropping attempts through fundamental quantum mechanical principles.

## Features

- **BB84 Protocol Simulation**: Complete implementation with random bit and basis selection
- **Eavesdropping Detection**: Simulates Eve's interception and measures quantum bit error rate (QBER)
- **Interactive Analysis**: Jupyter notebooks with detailed explanations and visualizations
- **Key Generation**: Demonstrates the sifting process to create shared secret keys
- **Security Analysis**: Shows how quantum mechanics provides information-theoretic security

## Files

### Interactive Infographic (`bb84/`)

- `index.html`: Interactive web-based infographic of the BB84 protocol
- `bb84.js`: JavaScript simulation logic and protocol implementation
- `style.css` and `satoshi.css`: Styling and visual design components
- `scroll-animations.js`: Animation framework for enhanced user experience

### `main.ipynb`

Main exercise notebook containing:

- Complete BB84 protocol implementation
- Step-by-step explanation of the quantum key distribution process
- Analysis of different interception rates and their effect on QBER
- Comparison with classical cryptography methods

### `lab.ipynb`

Laboratory version with enhanced features:

- Modified code focusing on actual key construction
- Detailed round-by-round analysis with basis matching
- Visual representation of the sifting process
- Error rate calculations and security threshold analysis

## How It Works

1. **Preparation**: Alice generates random bits and encodes them using random polarization bases
2. **Transmission**: Quantum states are sent through a quantum channel to Bob
3. **Measurement**: Bob measures using randomly chosen bases
4. **Sifting**: Alice and Bob publicly compare bases and keep only matching measurements
5. **Error Detection**: A subset of the key is compared to estimate the error rate (QBER)
6. **Security Check**: If QBER is below threshold (~11%), the key is considered secure

## Requirements

```bash
pip install pandas jupyter numpy
```

## Usage

### For the Interactive Infographic:

1. Open `bb84/index.html` in your web browser
2. Navigate through the interactive educational content

### For the Jupyter Notebooks:

1. Clone the repository
2. Install dependencies
3. Open either notebook in Jupyter:
   ```bash
   jupyter notebook main.ipynb
   # or
   jupyter notebook lab.ipynb
   ```
4. Execute the cells to observe the BB84 simulation in action

## Key Concepts Demonstrated

- **Quantum No-Cloning Theorem**: Quantum states cannot be copied perfectly
- **Measurement Disturbance**: Any eavesdropping attempt introduces detectable errors
- **Information-Theoretic Security**: Security based on physics, not computational complexity
- **QBER Analysis**: Quantum Bit Error Rate as a security metric

## Educational Value

This simulation facilitates understanding of:

- How quantum mechanics enables unconditionally secure communication
- The fundamental differences between classical and quantum cryptography
- Real-world limitations and advantages of QKD systems
- The role of error rates in quantum communication security

## Author

Adrian Rodriguez, 2025

---

_Note: This is a simulation for educational purposes. Real QKD implementations require specialized quantum hardware and more sophisticated error correction protocols._
