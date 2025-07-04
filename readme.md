# Project Default Stages Module - Installation Guide

## Directory Structure

Create the following directory structure in your Odoo addons folder:

```
project_default_stages/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── project.py
```

## File Contents

### 1. `__init__.py` (root directory)
```python
from . import models
```

### 2. `models/__init__.py`
```python
from . import project
```

### 3. Installation Steps

1. **Create the module folder** in your Odoo addons directory:
   ```bash
   mkdir /path/to/odoo/addons/project_default_stages
   ```

2. **Copy the files** from the code artifact into the appropriate locations

3. **Update the addons list** in Odoo:
   - Go to Apps menu
   - Click "Update Apps List"
   - Search for "Project Default Stages"
   - Install the module

4. **Alternative installation via command line**:
   ```bash
   # Restart Odoo with update
   ./odoo-bin -u project_default_stages -d your_database_name
   ```

## How It Works

- **Automatic Creation**: When you create a new project, the module automatically creates the 8 default stages
- **Fully Editable**: All stages can be renamed, reordered, or deleted after creation
- **Conditional Logic**: Only creates stages if the project doesn't already have any stages
- **Proper Sequencing**: Stages are created with logical sequence numbers
- **Folding**: The "DONE" stage is folded by default to keep the kanban view clean

## Customization Options

### Modify Default Stages
Edit the `default_stages` list in `models/project.py` to customize:
- Stage names
- Sequence order
- Folding behavior

### Add Stage Colors
You can extend the stage creation to include colors:
```python
{'name': 'BLOCKED', 'sequence': 5, 'fold': False, 'legend_blocked': 'Blocked tasks'}
```

### Add Stage Descriptions
```python
{'name': 'QAT', 'sequence': 6, 'fold': False, 'description': 'Quality Assurance Testing'}
```

## Testing

1. Create a new project
2. Check that all 8 stages appear in the project's kanban view
3. Verify that stages are editable (rename, delete, reorder)
4. Create another project to ensure it works consistently

## Troubleshooting

- **Module not appearing**: Make sure to update the apps list
- **Stages not created**: Check Odoo logs for any errors
- **Permission issues**: Ensure the user has project creation rights
