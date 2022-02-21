/*
본인의 이름을 char에 각각 선언 및 초기화하여,
유니코드 값을 구하여 16진수로 출력하는 함수를 작성하시오.
(배점: 30점)
[조건]
• 이름의 char를 유니코드로 형변환하지 말고,
유니코드값의 Character.MIN_VALUE 부터
Character.MAX_VALUE 까지를 반복하면서 코드값을 비교할 것
ex)
아래 코드형태처럼 구현하지 말것
char name1 = '박';
int charInt = (int)char;
• 반복문은 한번만 사용할 것
• 반복문을 사용할때,
이름의 코드값을 모두 찾았으면,
더이상 반복문을 실행하지 않고 종료할 것
• 이름이 박규태 일때,
[출력값]
0xBC15,
0xADDC,
0xD0DC
*/

public class Char01 {
	public static void main(String[] args) {
		char name1 = '김';
		char name2 = '하';
		char name3 = '림';
		int count = 0;
		
		for (int i = Character.MIN_VALUE; i <= Character.MAX_VALUE; i++) {
			if (name1 == i || name2 == i || name3 == i) {
				System.out.printf("%#X\n", i);
				count += 1;
			}
			if (count == 3) {
				break;
			}
		}
	}
}
