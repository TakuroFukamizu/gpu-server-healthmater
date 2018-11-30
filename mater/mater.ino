
const int meterPin = 9;
//const int val_max = 9;
const int valMax = 14;

void setup() {
  Serial.begin(9600);

  //初期設定
  analogWrite( meterPin, valMax );
  delay( 1000 );
  analogWrite( meterPin, valMax/2 );
  delay( 1000 );
  analogWrite( meterPin, 0 );
}

void loop() {
  if (!Serial.available() > 0) return; // データを受信した場合にのみ
  
//  int incomingByte = Serial.read();
//  if (incomingByte == -1) return;
//  if (incomingByte != 0xFF) {
//    Serial.write("not header value");
//    return; // not header value
//  }
  
  int gpuValue = Serial.read();
//  if (gpuValue == -1) return;
  if (gpuValue < 0 || 100 < gpuValue){
    Serial.write("out of range");
    return; //out of range
  }
  
  int pwmValue = gpuValue / (100 / valMax); //レンジを合わせる
  Serial.write(gpuValue);
  if (0 < pwmValue) {
    analogWrite( meterPin, pwmValue-1 );
    delay( 30 );
  }
  analogWrite( meterPin, pwmValue );
}