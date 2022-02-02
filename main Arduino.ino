
int a = 2;
int b = 3;
int c = 4;
int d = 5;

int aData = 0;
int bData = 0;
int cData = 0;
int dData = 0;

int hData = 0;
int iData = 0;
int jData = 0;

int data = 0;

int count = 0;
int htorF = 0;
void setup() {
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);

  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);

  Serial.begin(9600);
  delay(100);
}

void loop() {
   if(Serial.available() > 0){
      data = Serial.read();
      Serial.println(data);
      
      if (data == '1'){
        if(aData == 0){
            aData = 1;
         }
         else{
            aData = 0;
         }
      }

      if (data == '2'){
        if(bData == 0){
            bData = 1;
         }
         else{
            bData = 0;
         }
      }

      if (data == '3'){
        if(cData == 0){
            cData = 1;
         }
         else{
            cData = 0;
         }
      }

      if (data == '4'){
        if(dData == 0){
            dData = 1;
         }
         else{
            dData = 0;
         }
      }

      if (data == '5'){   
        aData = 0;
        bData = 0;
        cData = 0;
        dData = 0;
      }

      if (data == '6'){
        if(hData == 0){
            hData = 1;
            count = 0;
         }
         else{
            hData = 0;
         }
      }

      if (data == '7'){
        if(iData == 0){
            iData = 1;
            count = 0;
         }
         else{
            iData = 0;
         }
      }

      if (data == '8'){
        if(jData == 0){
            jData = 1;
            count = 0;
         }
         else{
            jData = 0;
         }
      }




      if(bData == 1){
        digitalWrite(b, LOW);
      }
      else{
        digitalWrite(b, HIGH);
      }

      if(cData == 1){
        digitalWrite(c, LOW);
      }
      else{
        digitalWrite(c, HIGH);
      }

      if(dData == 1){
        digitalWrite(d, LOW);
      }
      else{
        digitalWrite(d, HIGH);
      }



      if (hData == '1'){
        count = count + 1;
      }

      if (count >= 1000){
        count = 0;
        if (htorF == 0){
          htorF = 1;
        }
        else{
          htorF = 0;
        }
      }

      if(htorF or aData == 1){
        digitalWrite(a, LOW);
      }
      else{
        digitalWrite(a, HIGH);
      }
      
   }
}
