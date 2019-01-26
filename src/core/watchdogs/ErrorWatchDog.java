package core.watchdogs;

import core.DAO;

import java.io.IOException;
import java.nio.file.*;

public class ErrorWatchDog implements Runnable {

    ErrorWatchDog() { (new Thread(this)).start(); }

    public void run() {
        Path path = DAO.pythonPath;
        System.out.println(path);
        try (final WatchService watchService = FileSystems.getDefault().newWatchService()) {
            final WatchKey watchKey = path.register(watchService, StandardWatchEventKinds.ENTRY_MODIFY);
            while (true) {
                final WatchKey wk = watchService.take();
                System.out.println(path.toString() + "/err");
                for (WatchEvent<?> event : wk.pollEvents()) {
                    //we only register "ENTRY_MODIFY" so the context is always a Path.
                    final Path changed = (Path) event.context();
                    System.out.println(changed);
                    if (changed.endsWith("err")) {
                        System.out.println("error has occurred");
                        DAO.controller.callErrSearch();
                    }
                }
                // reset the key
                boolean valid = wk.reset();
                if (!valid) {
                    System.out.println("Key has been unregisterede");
                }
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}

