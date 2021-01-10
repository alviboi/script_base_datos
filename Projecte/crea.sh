#!/bin/bash
pandoc Projecte.md -o projecte.pdf --from markdown+implicit_figures --template eisvogel --listings --filter pandoc-latex-environment --number-sections
