"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

# from xblock.fields import Integer, Scope, String, Any, Boolean, Dict
from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class paellainteractiveXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    href = String(display_name="href",
                  default="mrbosy/mrbosy.xml",
                  scope=Scope.content,
                  help="Interactive Video in Paella Player")

    display_name = String(display_name="Display Name",
                          default="Paella Interactive Video Player",
                          scope=Scope.settings,
                          help="Name of the component in the edxplatform")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    @XBlock.json_handler
    def save_paella(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        #assert data['hello'] == 'world'
        self.href = data['href']
        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    def student_view(self, context=None):
        """
        The primary view of the paellainteractiveXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/paellainteractivevideo.html")
        frag = Fragment(html.format(self=self))
        return frag

    # TO-DO: change this view to display your data your own way.
    def studio_view(self, context=None):
        """
        The primary view of the paellainteractiveXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/paellainteractivevideo_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/paellainteractivevideo.js"))
        frag.initialize_js('paellainteractiveXBlock')
        return frag

    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("paellainteractiveXBlock",
             """<vertical_demo>
                <paellainteractivevideo/>
                </vertical_demo>
             """),
        ]