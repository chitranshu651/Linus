package core;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception{
        FXMLLoader loader = new FXMLLoader(getClass().getResource("home.fxml"));
        Parent root = loader.load();
        DAO.controller = loader.getController(); //save controller instance for calling updateGUI method from DAO
        primaryStage.initStyle(StageStyle.TRANSPARENT);
        Scene scene = new Scene(root, 600, 560);
        scene.setFill(Color.TRANSPARENT);
        scene.getStylesheets().add(getClass().getResource("customTransparency.css").toExternalForm());
        primaryStage.setScene(scene);
        primaryStage.setMinWidth(600);
        primaryStage.setMaxWidth(600);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
