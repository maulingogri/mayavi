# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.plot import Plot


class ScalarsToColorsItem(Plot):
    """
    ScalarsToColorsItem - Abstract class for scalars_to_colors items.
    
    Superclass: Plot
    
    ScalarsToColorsItem implements item bounds and painting for
    inherited classes that provide a texture (_compute_texture()) and
    optionally a shape
    
    See Also:
    
    ControlPointsItem LookupTableItem ColorTransferFunctionItem
    CompositeTransferFunctionItem PiecewiseItemFunctionItem
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarsToColorsItem, obj, update, **traits)
    
    mask_above_curve = traits.Bool(False, help=\
        """
        
        """
    )
    def _mask_above_curve_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaskAboveCurve,
                        self.mask_above_curve)

    def _get_poly_line_pen(self):
        return wrap_vtk(self._vtk_obj.GetPolyLinePen())
    poly_line_pen = traits.Property(_get_poly_line_pen, help=\
        """
        Get a pointer to the Pen object that controls the drawing of
        the edge of the shape if any. poly_line_pen type is Pen::NO_PEN
        by default.
        """
    )

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('use_index_for_x_series',
    'GetUseIndexForXSeries'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('visible', 'GetVisible'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('mask_above_curve', 'GetMaskAboveCurve'), ('width', 'GetWidth'),
    ('label', 'GetLabel'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'label', 'mask_above_curve',
    'opacity', 'use_index_for_x_series', 'visible', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarsToColorsItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarsToColorsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['label', 'mask_above_curve', 'opacity',
            'use_index_for_x_series', 'visible', 'width']),
            title='Edit ScalarsToColorsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarsToColorsItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
