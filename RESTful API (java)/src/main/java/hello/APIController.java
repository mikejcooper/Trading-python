package hello;

import org.json.JSONObject;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.atomic.AtomicLong;

@RestController
public class APIController {

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @RequestMapping("/buy")
    public Buy buy(@RequestParam(value="stock", defaultValue="World") JSONObject test) {

        System.out.print(test);


        return new Buy(counter.incrementAndGet(),
                            String.format(template, test));
    }
}
