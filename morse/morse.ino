char m, *msg = "-. --- - .... .. -. --. / ";
int x1 = 400, x2 = 2*x1, x3 = 3*x1;

void setup() {
  DDRD |= (1 << 2);
}

void loop() {
  for (int i = 0; m = msg[i]; ++i) {
    if (m == ' ' || m == '/') {
      delay(x2);
    }
    else {
      for (int j = 0; j < 2; ++j) {
        PORTD ^= (1 << 2);
        delay((m == '.' || j) ? x1 : x3);
      }
    }
  }
}
