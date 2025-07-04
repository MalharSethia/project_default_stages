from odoo import models, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.model_create_multi
    def create(self, vals_list):
        """Override create method to add default stages when project is created"""
        projects = super().create(vals_list)
        
        # Define default stages
        default_stages = [
            {'name': 'BACKLOG', 'sequence': 1, 'fold': False},
            {'name': 'TO-DO', 'sequence': 2, 'fold': False},
            {'name': 'IN PROGRESS', 'sequence': 3, 'fold': False},
            {'name': 'WAITING', 'sequence': 4, 'fold': False},
            {'name': 'BLOCKED', 'sequence': 5, 'fold': False},
            {'name': 'QAT', 'sequence': 6, 'fold': False},
            {'name': 'UAT', 'sequence': 7, 'fold': False},
            {'name': 'DONE', 'sequence': 8, 'fold': True},
        ]
        
        for project in projects:
            # Only create default stages if the project doesn't have any stages yet
            if not project.type_ids:
                stage_vals = []
                for stage_data in default_stages:
                    stage_vals.append({
                        'name': stage_data['name'],
                        'sequence': stage_data['sequence'],
                        'fold': stage_data['fold'],
                        'project_ids': [(6, 0, [project.id])],
                    })
                
                # Create all stages at once
                self.env['project.task.type'].create(stage_vals)
        
        return projects
