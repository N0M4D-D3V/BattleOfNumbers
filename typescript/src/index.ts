import { IOService } from "./utils/io.service";

const io = new IOService();
io.ask("Hola, como te llamas?").then((res) => {
  console.log("Encantado de conocerte, ", res);
});
