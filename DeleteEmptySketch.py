# =============================================================================
# Add-In Name    : DeleteEmptySketch
# Author         : Rohit Bapat
# Email          : rhtbapat@gmail.com
# Description    : Automatically deletes any empty sketch (no curves, no
#                  dimensions, no text) when the user clicks Finish Sketch.
#                  Simply run the add-in to enable the behaviour and stop it
#                  to disable it. No configuration required.
# =============================================================================

import adsk.core
import adsk.fusion
import os

_app = None
_ui = None
_handler = None
_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'run.log')


class _Handler(adsk.core.ApplicationCommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        try:
            if args.commandId != 'SketchStop':
                return
            design = adsk.fusion.Design.cast(_app.activeProduct)
            if not design:
                return
            comp = design.activeComponent
            to_delete = []
            for i in range(comp.sketches.count):
                sk = comp.sketches.item(i)
                c = sk.sketchCurves
                total = (c.sketchLines.count +
                         c.sketchCircles.count +
                         c.sketchArcs.count +
                         c.sketchEllipses.count +
                         c.sketchFittedSplines.count +
                         c.sketchFixedSplines.count +
                         c.sketchConicCurves.count)
                if total == 0 and sk.sketchDimensions.count == 0 and sk.sketchTexts.count == 0:
                    to_delete.append(sk)
            with open(_LOG, 'a') as f:
                f.write(f'SketchStop: found {len(to_delete)} empty sketch(es): {[s.name for s in to_delete]}\n')
            for sk in to_delete:
                sk.deleteMe()
        except Exception as e:
            with open(_LOG, 'a') as f:
                f.write(f'ERROR: {e}\n')


def run(context):
    global _app, _ui, _handler
    _app = adsk.core.Application.get()
    _ui = _app.userInterface
    _handler = _Handler()
    _ui.commandTerminated.add(_handler)
    with open(_LOG, 'w') as f:
        f.write('run() called\n')


def stop(context):
    global _handler
    if _handler and _app:
        _app.userInterface.commandTerminated.remove(_handler)
    _handler = None
