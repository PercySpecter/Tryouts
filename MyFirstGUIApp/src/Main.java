
import javafx.application.*;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.*;


public class Main extends Application
{
	Stage stage;
	Scene scene1 , scene2;
	
	
	public static void main(String args[])
	{
		launch(args);
	}
	
	@Override
	public void start(Stage primaryStage) throws Exception
	{
		stage = primaryStage;
		stage.setTitle("Switching Scenes");
		
		Label label1 = new Label("Hello!");
		Button button1 = new Button("CLICK ME");
		button1.setPrefSize(200 , 200);
		button1.setOnAction(e -> stage.setScene(scene2));
		
		StackPane layout1 = new StackPane(); 
		layout1.getChildren().setAll(label1 , button1);
		scene1 = new Scene(layout1 , 1366 , 768);
		
		Button button2 = new Button("Have a Good Day!!");
		button2.setPrefSize(200 , 200);
		button2.setOnAction(e -> stage.setScene(scene1));
		
		StackPane layout2 = new StackPane();
		layout2.getChildren().setAll(button2);
		scene2 = new Scene(layout2 , 1366 , 768);
		
		stage.setScene(scene1);
		stage.show();
	}
}
