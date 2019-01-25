package core;

import com.jfoenix.controls.*;
import javafx.fxml.FXML;

public class Controller {

    @FXML
    private JFXButton goButton;

    @FXML
    private JFXTextField inputField;

    public void action() {
        if(inputField.getText().equals("")) {
            return;
        }
        System.out.println(inputField.getText());
    }

}
