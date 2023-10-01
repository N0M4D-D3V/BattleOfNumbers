"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const io_service_1 = require("./utils/io.service");
const io = new io_service_1.IOService();
io.ask("Hola, como te llamas?").then((res) => {
    console.log("Encantado de conocerte, ", res);
});
