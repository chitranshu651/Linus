package core;

import core.template.Image;
import core.template.Text;
import core.template.URI;

import java.util.Iterator;
import java.util.List;

/**
 * GSON read output and instantiate this class object.
 * Output class represents blueprint of output
 */
public class Output {
    String title;
    List<Integer> order;
    List<Image> Image;
    List<URI> URI;
    List<Text> Text;
    String command;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<Integer> getOrder() {
        return order;
    }

    public void setOrder(List<Integer> order) {
        this.order = order;
    }

    public List<core.template.Image> getImage() {
        return Image;
    }

    public void setImage(List<core.template.Image> image) {
        Image = image;
    }

    public List<core.template.URI> getURI() {
        return URI;
    }

    public void setURI(List<core.template.URI> URI) {
        this.URI = URI;
    }

    public List<core.template.Text> getText() {
        return Text;
    }

    public void setText(List<core.template.Text> text) {
        Text = text;
    }

    public String getCommand() { return command; }

    public void setCommand(String title) { this.command = command; }
}
