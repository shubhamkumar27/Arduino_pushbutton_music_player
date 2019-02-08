int playb = 2;
int pauseb = 3;
int replayb = 4;

void setup() {
  // put your setup code here, to run once:
pinMode(playb,OUTPUT);
pinMode(pauseb,OUTPUT);
pinMode(replayb,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int play = digitalRead(playb);
if(play == 1){
  Serial.println("play");}
delay(200);

int pause= digitalRead(pauseb);
if(pause == 1){
  Serial.println("pause");}
delay(50);

int replay = digitalRead(replayb);
if (replay == 1){
  Serial.println("replay");
  delay(50);}
}
