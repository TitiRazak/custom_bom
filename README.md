# CUSTOM BOM Module for Odoo

## Overview
The CUSTOM BOM module extends the functionality of the Manufacturing (mrp) and Sales (sale) modules in Odoo by adding the sale price of products directly from the Bill of Materials (BOM). This module is particularly useful for manufacturing businesses that require a quick and accurate calculation of product costs based on their BOMs.

## Features
- **Price Unit Calculation**: Automatically computes the unit price for each BOM line based on the product's sale price.
- **Subtotal Computation**: Calculates the subtotal for each BOM line by multiplying the unit price with the product quantity.
- **Total Price Calculation**: Aggregates the subtotals of all BOM lines to compute the total price of the BOM.

## Installation
To install this module, you need to:
1. Clone the repository into your Odoo addons path.
2. Update the module list in Odoo.
3. Install the module by navigating to Apps > CUSTOM BOM and clicking the 'Install' button.

## Dependencies
This module depends on the following Odoo modules:
- `base`
- `mrp`
- `sale`
- `product`

Ensure these modules are installed and up-to-date before installing the CUSTOM BOM module.

## Usage
Once installed, the module will automatically add new fields to the BOM line and BOM models. The prices will be computed whenever a product is selected or the quantity is changed in the BOM line.

## License
This module is published under the LGPL-3 license, allowing you to use and distribute it within the terms of this license.

## Support
If you encounter any issues or have questions regarding the module, please create an issue in the repository or contact the maintainer.

## Contributing
Contributions are welcome! If you would like to contribute, please fork the repository, make your changes, and submit a pull request.

