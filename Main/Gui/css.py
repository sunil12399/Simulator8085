# Main= 67e1ff
# secondary = 3f51b5 dark
# tertiary = f8feff light
# quarter = e9fbff lighter
stylesheet = """
QMainWindow{
background-color: #e9fbff
}
  QToolBar {
      background: white;
      spacing: 3px; /* spacing between items in the tool bar */
  }
  QTabWidget::pane { /* The tab widget frame */
      border-top: 2px solid #C2C7CB;
  }

  QTabWidget::tab-bar {
      left: 5px; /* move to the right by 5px */
  }

  /* Style the tab using the tab sub-control. Note that
      it reads QTabBar _not_ QTabWidget */
  QTabBar::tab {
      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                  stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
      border: 2px solid #C4C4C3;
      border-bottom-color: #C2C7CB; /* same as the pane color */
      border-top-left-radius: 4px;
      border-top-right-radius: 4px;
      min-width: 8ex;
      padding: 2px;
  }

  QTabBar::tab:selected, QTabBar::tab:hover {
      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                  stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                  stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
  }

  QTabBar::tab:selected {
      border-color: #9B9B9B;
      border-bottom-color: #C2C7CB; /* same as pane color */
  }

  QTabBar::tab:!selected {
      margin-top: 2px; /* make non-selected tabs look smaller */
  }

  /* make use of negative margins for overlapping tabs */
  QTabBar::tab:selected {
      /* expand/overlap to the left and right by 4px */
      margin-left: -4px;
      margin-right: -4px;
  }

  QTabBar::tab:first:selected {
      margin-left: 0; /* the first selected tab has nothing to overlap with on the left */
  }

  QTabBar::tab:last:selected {
      margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
  }
"""
