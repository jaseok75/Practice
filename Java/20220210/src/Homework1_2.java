/*수강관리 하는 프로그램을 작성하기 위한 메뉴 기능을 구현 하고자 한다. 아래 조건과 예시를 보고 프로그램을

작성하시오.
(배점: 30점)
[조건]
• 숫자만 입력하고 그외 입력은 하지 않는 것을 전제로 한다.
• 입력은 Scanner 클래스의 nextInt 함수를 이용한다.

시작화면

[메뉴선택]
1.회원 관리
2.과목 관리
3.수강 관리
4.결제 관리
5.종료

“1” 입력 후 엔터 à “회원 관리 메뉴를 선택했습니다.” 문자열 출력
“2“ 입력 후 엔터 à “과목 관리 메뉴를 선택했습니다.” 문자열 출력
“3“ 입력 후 엔터 à “수강 관리 메뉴를 선택했습니다.” 문자열 출력
“4“ 입력 후 엔터 à “결제 관리 메뉴를 선택했습니다.” 문자열 출력
이후, 다시 시작 화면을 보여 줌.
“5” 입력 후 엔터 à “프로그램을 종료합니다.” 문자열 출력 후 프로그램 종료*/

import java.util.Scanner;

public class Char01 {
	public static void main(String[] args) {
		while(true) {
			Scanner sc = new Scanner(System.in);
			System.out.println("[메뉴선택]");
			System.out.println("1.회원 관리\n2.과목 관리\n3.수강 관리\n4.결제 관리\n5.종료");
			int input = sc.nextInt();
			
			if (input == 1) {
				System.out.println("회원 관리 메뉴를 선택했습니다.");
			}
			else if (input == 2) {
				System.out.println("과목 관리 메뉴를 선택했습니다.");
			}
			else if (input == 3) {
				System.out.println("수강 관리 메뉴를 선택했습니다.");
			}
			else if (input == 4) {
				System.out.println("결제 관리 메뉴를 선택했습니다.");
			}
			else if (input == 5) {
				System.out.println("프로그램을 종료합니다.");
				break;
			}
		}
	}
}
