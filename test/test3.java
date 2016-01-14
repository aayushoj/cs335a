import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.*;
import javax.accessibility.*;
import com.sun.java.accessibility.util.*;

public class AssistiveExample extends JPanel
  implements MouseMotionListener, ActionListener, GUIInitializedListener {


  public void guiInitialized() {
    createGUI();
  }

  public void createGUI() {
    //  We want to track the mouse motions, so notify the
    //  Swing event monitor of this.
    SwingEventMonitor.addMouseMotionListener(this);

    //  Start a Timer object to measure how long the mouse stays
    //  over a particular area.
    timer = new Timer(500, this);
  }

  public void mouseMoved(MouseEvent e) {
    //  If the mouse moves, restart the timer.
    timer.restart();
  }
  public void mouseDragged(MouseEvent e) {
    //  If the mouse is dragged, restart the timer.
    timer.restart();
  }

  public void actionPerformed(ActionEvent e) {
    //Find the component currently under the mouse.
    Point currentPosition = EventQueueMonitor.getCurrentMousePosition();
    Accessible comp = EventQueueMonitor.getAccessibleAt(currentPosition);

    //If the user pressed the button, and the component
    //has an accessible action, then execute it.
    if (e.getActionCommand() == "Perform Action") {
      AccessibleContext context = comp.getAccessibleContext();
      AccessibleAction action = context.getAccessibleAction();

      if (action != null)
        action.doAccessibleAction(0);
      else
        System.out.println("No accessible action present!");
      return;
    }

    //  Otherwise, the timer has fired. Stop it and update the window.
    timer.stop();
    updateWindow(comp);
  }

  private void updateWindow(Accessible component) {
    if (component == null) { return; }

    // Reset the check boxes
    actionCheckBox.setSelected(false);
    selectionCheckBox.setSelected(false);
    textCheckBox.setSelected(false);
    componentCheckBox.setSelected(false);
    valueCheckBox.setSelected(false);
    hypertextCheckBox.setSelected(false);
    iconCheckBox.setSelected(false);
    tableCheckBox.setSelected(false);
    editableTextCheckBox.setSelected(false);

    // Get the accessibile context of the component in question
    AccessibleContext context = component.getAccessibleContext();
    AccessibleRelationSet ars = context.getAccessibleRelationSet();

    nameLabel.setText("Name: " + context.getAccessibleName());
    descriptionLabel.setText("Desc: " +  context.getAccessibleDescription());
    relationLabel.setText("Relation: " + ars);

    // Check the context for each of the accessibility types
    if (context.getAccessibleAction() != null)
      actionCheckBox.setSelected(true);
    if (context.getAccessibleSelection() != null)
      selectionCheckBox.setSelected(true);
    if (context.getAccessibleText() != null) {
      textCheckBox.setSelected(true);
      if (context.getAccessibleText() instanceof AccessibleHypertext)
        hypertextCheckBox.setSelected(true);
    }
    if (context.getAccessibleComponent() != null) {
      componentCheckBox.setSelected(true);
      classLabel.setText("Class: " + context.getAccessibleComponent());
      parentLabel.setText("Parent: " + context.getAccessibleParent());
    }
    if (context.getAccessibleValue() != null)
      valueCheckBox.setSelected(true);
    if (context.getAccessibleIcon() != null)
      iconCheckBox.setSelected(true);
    if ((context.getAccessibleTable() != null) ||
        (context.getAccessibleParent() instanceof JTable)) {
      tableCheckBox.setSelected(true);
      tableLabel.setText("Table Desc: " +
          context.getAccessibleParent().getAccessibleContext()
                 .getAccessibleDescription());
    }
    else {
      tableLabel.setText("");
    }
    // On 1.4+ systems, you can check for editable text with these two lines.
    // Note that because of the 1.4 restriction, these lines will not compile
    // on a Mac system as of the time of this writing.  You can comment out
    // these lines and still compile/run the example, though.
    //if (context.getAccessibleEditableText() != null)
    //  editableTextCheckBox.setSelected(true);
    repaint();
  }
}




/*      Java Swing, Second Edition
 *      Tips and Tools for Killer GUIs
 *    By Marc Loy, Robert Eckstein, Dave Wood, James Elliott, Brian Cole
 *      Second Edition November 2002
 *      http://www.oreilly.com/catalog/jswing2/
 */
