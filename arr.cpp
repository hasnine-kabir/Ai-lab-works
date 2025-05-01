#include <bits/stdc++.h>
using namespace std;

int main() {
    double r1,r2,r3,a,b,c,s,t1,t2,t3,area,x1,x2,x3,ans;
    cin >> r1 >> r2 >> r3;
    a = r1+r2;
    b = r2+r3;
    c = r1+r3;

    s = (a + b + c) / 2;

    area = sqrt(s * (s - a) * (s - b) * (s - c));

    t1 = acos((b*b + c*c - a*a) / (2*b*c));
    t2 = acos((a*a + c*c - b*b) / (2*a*c));
    t3 = acos((a*a + b*b - c*c) / (2*a*b));

    x1 = 0.5*r1*r1*t1;
    x2 = 0.5*r2*r2*t2;
    x3 = 0.5*r3*r3*t3;

    ans= area - (int(x1 + x2 + x3));
    
    cout << ans << endl;

    return 0;
}
