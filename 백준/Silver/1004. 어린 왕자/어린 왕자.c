#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);

	int sx, sy;
	int dx, dy;
	int numPnt;
	int px, py, pr;
	int sdist, ddist;
	int cnt = 0;

	
	while (t--) {
		scanf("%d %d %d %d", &sx, &sy, &dx, &dy);
		scanf("%d", &numPnt);

		while (numPnt--) {
			scanf("%d %d %d", &px, &py, &pr);

			sdist = (sx - px) * (sx - px) + (sy - py) * (sy - py);
			ddist = (dx - px) * (dx - px) + (dy - py) * (dy - py);
			if (sdist < pr * pr && ddist > pr * pr)
				cnt++;
			else if (sdist > pr * pr && ddist < pr * pr)
				cnt++;

		}
		printf("%d\n", cnt);
		cnt = 0;
	}

	return 0;
}