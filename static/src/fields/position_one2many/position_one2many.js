/** @odoo-module */

import {_t} from "@web/core/l10n/translation";
import {registry} from "@web/core/registry";

import {formatDate} from "@web/core/l10n/dates";

import {SkillsX2ManyField, skillsX2ManyField} from "@hr_skills/fields/skills_one2many/skills_one2many";
import {CommonSkillsListRenderer} from "@hr_skills/views/skills_list_renderer";

export class PositionListRenderer extends CommonSkillsListRenderer {
    get groupBy() {
        return 'date_start';
    }


    get colspan() {
        if (this.props.activeActions) {
            return 3;
        }
        return 2;
    }

    formatDate(date) {
        return formatDate(date);
    }

    setDefaultColumnWidths() {
    }
}

PositionListRenderer.template = 'hr_skills.PositionListRenderer';
PositionListRenderer.rowsTemplate = "hr_skills.PositionListRenderer.Rows";
PositionListRenderer.recordRowTemplate = "hr_skills.PositionListRenderer.RecordRow";

export class PositionX2ManyField extends SkillsX2ManyField {
    getWizardTitleName() {
        return _t("Create a position line");
    }

}

PositionX2ManyField.components = {
    ...SkillsX2ManyField.components,
    ListRenderer: PositionListRenderer,
};

export const positionX2ManyField = {
    ...skillsX2ManyField,
    component: PositionX2ManyField,
};

registry.category("fields").add("position_one2many", positionX2ManyField);
