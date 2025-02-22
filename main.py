import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bfem.template.MyApp import MyApp


if __name__ == '__main__':
    MyApp().run()
    


