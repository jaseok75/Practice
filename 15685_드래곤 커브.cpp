/*
Project: 백준_15685_드래곤 커브
Date: 2022.03.29.화.
Comment:
- 삼성 기출 문제
*/

#include <iostream>
#include <deque>

using namespace std;

struct Rect_Pos {
	int x;
	int y;
};

static int dx[4] = { 0, -1, 0, 1 };
static int dy[4] = { 1, 0, -1, 0 };
deque<Rect_Pos> rect;

int isRect(Rect_Pos pos) {
	deque<Rect_Pos>::iterator iter;

	if (rect.empty()) {
		return true;
	}

	for (iter = rect.begin(); iter != rect.end(); iter++) {
		if (pos.x == iter->x && pos.y == iter->y) {
			return false;
		}
	}

	return true;
}

void turn90(Rect_Pos pos, int g, deque<int> direct, int board[101][101]) {
	for (int i = 0; i < g; i++) {
		int turn_size = direct.size();
		for (int j = 0; j < turn_size; j++) {
			int turn = (direct[turn_size - 1 - j] + 1) % 4;
			Rect_Pos n_pos;
			n_pos.x = pos.x + dx[turn];
			n_pos.y = pos.y + dy[turn];
			if (0 <= n_pos.x && n_pos.x < 101 && 0 <= n_pos.y && n_pos.y < 101) {
				board[n_pos.x][n_pos.y] = 1;
				if (isRect(n_pos)) {
					rect.push_back(n_pos);
				}
			}
			pos.x = n_pos.x;
			pos.y = n_pos.y;
			direct.push_back(turn);
		}
	}
}

int rect_check(int board[101][101]) {
	int rect_x[3] = { 0, 1, 1 };
	int rect_y[3] = { 1, 1, 0 };
	int rect_count = 0;
	while (!rect.empty()) {
		Rect_Pos pos = rect.front();
		rect.pop_front();
		int is_rect = 0;
		for (int i = 0; i < 3; i++) {
			Rect_Pos n_pos;
			n_pos.x = pos.x + rect_x[i];
			n_pos.y = pos.y + rect_y[i];
			if (0 <= n_pos.x && n_pos.x < 101 && 0 <= n_pos.y && n_pos.y < 101 && board[n_pos.x][n_pos.y] == 1) {
				is_rect += 1;
			}
			else
				break;
		}
		if (is_rect == 3) {
			rect_count++;
		}
	}
	return rect_count;
}

int main() {
	int n;
	int board[101][101] = { 0 };

	cin >> n;
	for (int i = 0; i < n; i++) {
		int y, x, d, g;
		deque<int> direct;
		Rect_Pos rect_pos;
		cin >> y >> x >> d >> g;
		rect_pos.x = x;
		rect_pos.y = y;
		board[x][y] = 1;
		if (isRect(rect_pos)) {
			rect.push_back(rect_pos);
		}
		rect_pos.x = x + dx[d];
		rect_pos.y = y + dy[d];
		if (0 <= rect_pos.x && rect_pos.x < 101 && 0 <= rect_pos.y && rect_pos.y < 101) {
			board[rect_pos.x][rect_pos.y] = 1;
			if (isRect(rect_pos)) {
				rect.push_back(rect_pos);
			}
		}
		direct.push_back(d);
		turn90(rect_pos, g, direct, board);
	}
	cout << rect_check(board);
	return 0;
}
