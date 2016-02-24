package definitions

func init() {
	add(`RuleItem`, &defRuleItem{})
}

type defRuleItem struct{}

func (*defRuleItem) String() string {
	return `
<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.19.0 -->
<interface>
  <requires lib="gtk+" version="3.16"/>
  <object class="GtkGrid" id="grid">
    <property name="visible">True</property>
    <property name="can_focus">False</property>
    <property name="hexpand">True</property>
    <child>
      <object class="GtkLabel" id="app_label">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="halign">start</property>
        <property name="margin_right">10</property>
        <property name="xalign">0</property>
      </object>
      <packing>
        <property name="left_attach">0</property>
        <property name="top_attach">0</property>
      </packing>
    </child>
    <child>
      <object class="GtkLabel" id="verb_label">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="margin_right">10</property>
        <property name="xalign">1</property>
      </object>
      <packing>
        <property name="left_attach">1</property>
        <property name="top_attach">0</property>
      </packing>
    </child>
    <child>
      <object class="GtkLabel" id="target_label">
        <property name="visible">True</property>
        <property name="can_focus">False</property>
        <property name="halign">start</property>
        <property name="hexpand">True</property>
        <property name="xalign">0</property>
      </object>
      <packing>
        <property name="left_attach">2</property>
        <property name="top_attach">0</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="edit_button">
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="relief">none</property>
        <signal name="clicked" handler="on_edit_rule" swapped="no"/>
        <child>
          <object class="GtkImage" id="image2">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="icon_name">document-properties-symbolic</property>
          </object>
        </child>
      </object>
      <packing>
        <property name="left_attach">3</property>
        <property name="top_attach">0</property>
      </packing>
    </child>
    <child>
      <object class="GtkButton" id="delete_button">
        <property name="visible">True</property>
        <property name="can_focus">True</property>
        <property name="receives_default">True</property>
        <property name="relief">none</property>
        <signal name="clicked" handler="on_delete_rule" swapped="no"/>
        <child>
          <object class="GtkImage" id="image1">
            <property name="visible">True</property>
            <property name="can_focus">False</property>
            <property name="icon_name">edit-delete-symbolic</property>
          </object>
        </child>
      </object>
      <packing>
        <property name="left_attach">4</property>
        <property name="top_attach">0</property>
      </packing>
    </child>
  </object>
</interface>

`
}
