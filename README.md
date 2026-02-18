# Arrhenius-diffusion-modeling


Project Overview:

Diffusion is a fundamental phenomenon in metallurgy, especially in processes such as carburizing, alloy homogenization, and heat treatment.
The diffusion coefficient (𝐷) varies with temperature and follows the Arrhenius equation.

        D = D0 * exp(-Q/RT)

where,  D = Diffusion Coefficient (m^2/sec)
        D0 = Diffusion Coefficient at 298K
        Q = Activation Energy
        R = Universal Gas Constant
        T = Absolute Temperature

This project transforms the nonlinear Arrhenius equation into a linear mathematical form and applies linear regression to estimate key diffusion parameters.

The objective is to integrate:
  -Core metallurgy concepts
  -Mathematical modeling
  -Basic machine learning (linear regression)

This project builds a bridge between materials science and data-driven analysis.


Methodology & Implementation:

  -Generated temperature data within a defined range.
  -Computed diffusion coefficient using the Arrhenius equation.
  -Transformed the data into linear form: x=1/T, 𝑦=ln𝐷
  -Implemented linear regression manually using NumPy.
  -Extracted activation energy and pre-exponential factor.
  -Validated results using graphical Arrhenius plot.


WORK COMPLETED: 

  -Mathematical modeling of temperature-dependent diffusion.
  -Linear transformation of nonlinear Arrhenius relation.
  -Linear regression implementation without ML libraries.
  -Parameter extraction (Q and D₀).
  -Visualization of regression fit.


LIMITATIONS OF CURRENT PROJECT:

Assumes ideal Arrhenius behavior & does not account for:

  -Grain boundary diffusion.
  -Phase transformations.
  -Composition-dependent diffusion.
  -Assumes constant diffusion coefficient at fixed temperature.

CONCLUSION:
This project demonstrates how classical metallurgy equations can be integrated with basic machine learning concepts. 
It provides a structured, physics-based approach for estimating diffusion parameters using regression while maintaining strong theoretical grounding.

The work is ongoing and aims to evolve into a more experimentally relevant predictive diffusion model.
