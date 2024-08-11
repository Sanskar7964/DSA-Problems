#include <bits/stdc++.h>
#include<iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define ll long long;
long long le18 = 1e18;

/*
int main(){
    ll n;
    cin >> n;

    cout << n;

    while(n>1){
        if(n%2==0)
             n/=2;

        else
             n= n*3+1;
        cout << " " <<n;

    }
} */

/* int main(){
    ll n, sum = 0;
    cin >> n;
    for (int i=1; i<n; ++i){
        int  a;
        cin>> a;

        sum+=a;

    }
    cout<< n*(n+1)/2-sum;

} */

/* int main() {
    string s;
    cin >> s;
     int ans = 1, c=0;
     char l = s[0];

     for(char d :  s){
        if (d==l){
            ++c;
            ans = max(c, ans);


        }
        else {
            l=d;
            c=1;

        }
     }
     cout << ans;

} */

/* int main (){
    ll n, c=0;
    cin >> n;
    int mx = 0;

    ll ans=0;

    for(int i=0; i<n; ++i){
        int x;
        cin >> x;

        mx = max(x,mx);

        ans+= mx-x;

    }  
    cout << ans;
    
} */

/* int main(){
    ll n;
    cin >> n;
    if(n==1){
        cout << 1;
        return 0; 

    }
    if (n==2 || n==3){
       cout << "NO SOLUTION"; 
       return 0;
    }

    if(n%2==0){
        for(int i=2; i<=n; i+=2)
        cout << i << " ";
        for(int i=1; i<=n; i+=2)
        cout << i << " ";

    }
    else {
        for(int i=1; i<=n; i+=2)
        cout << i << " ";

        for(int i=2; i<=n; i+=2)
        cout << i << " ";
    }


} */

/* int main(){
    ll n;
    cin >> n;
    
    for(int k=1; k<=n; ++k){
        ll a1 = k*k; ll a2 = a1*(a1-1)/2;
        if(k>2)
            a2-= 4*(k-1)*(k-2);
        cout << a2 << "\n";
    }
} */

// 1234567 curr_sum = 0, target_sum = total_sum/2
// 
/* int main(){
    ll n;
    cin >> n;
    ll sum = n*(n+1)/2;
    if(sum%2 !=0){
        cout << "NO";
        return 0;
    }
    ll targ_sum = sum/2;
    ll curr_sum =0;
    vector<ll> v1, v2;

    for(int i = n; i>=1; --i){
        if(curr_sum+i <= targ_sum){ v1.push_back(i);
           curr_sum += i;
    }
        else {
            v2.push_back(i);
        }
    
        
    }

    cout << "YES\n";
    cout << v1.size() << "\n";
    for(ll i:v1)
        cout << i << " ";
    cout << "\n";
    cout << v2.size() << "\n";
    for(ll i : v2)
        cout << i << " ";

    cout << "\n";    

} */

/* int main(){
    const int MOD = 1000000007;

    ll n;
    cin >> n;
    int count_bits(int n) {
        
            return std::pow(2,n)% MOD;
    }
} */

//12! prime factorization in 2, 5 format count number of 5 factors.
/* int main(){
    ll n;
    cin >> n;
    ll ans = 0;
    for(ll i=5; i<=n; i*=5){
        ans += n/i;

    }
    cout << ans;
} */

//modulo of a+b multiple of 3 and rest make sense;
/* int main(){
    ll t;
    cin >> t;
    while(t--){
        int  a, b;
        cin >> a >> b; 
        if((a+b)%3==0 && 2*b>=a && 2*a>=b )
            cout << "YES";
        else
            cout << "NO";
        cout << "\n";
    }
   
}

 */

//AAAACACBA

/* int main(){
    string s;
    cin >> s;
    unordered_map<char,int> char_count;
    char odd_char = '\0';

    for (char c: s){
        char_count[c]++;
        if(char_count[c]%2 ==1 ){
            if(odd_char != '\0'){
               cout << "NO SOLUTION";
               return 0;
            }
            odd_char = c;

        }
    }

    string result;
        for (auto const& [char_, count] : char_count) {
        if (char_ != odd_char) {
        result.append(count / 2, char_);
        }
    } 
    cout << result;
    if(odd_char!='\0'){
        cout << odd_char;

    }
    cout << string(result.rbegin(), result.rend());
    return 0;
} */

// 3 

/* int main(){
    string str;
    cin >> str;
    vector<string> sol;
    do{
        sol.push_back(str);
    }
    while(next_permutation(str.begin(), str.end()));
    cout << sol.size() <<'\n';
    for(string c:sol)
        cout << c << '\n';

    
} */

// 32741
/* 
This is a crucial bitmasking method for subsets finding of a string of numbers;

int main() {
    int n;
    int ts = 0;
    cin >> n;
    vector<int> p(n); // Declare a single vector p of size n

    for(int i = 0; i < n; i++) {
        cin >> p[i]; // Read each element of p
        ts += p[i]; // Calculate the total sum ts
    }

    long long ans = le18; // Correct the type of ans

    for(int mask = 0; mask < (1 << n); mask++) { // Add curly braces for loop body
        long long sumA = 0; // Declare sumA and sumB inside the loop
        long long sumB = 0;

        for(int pos = 0; pos < n; pos++) {
            if(mask & (1 << pos)) {
                sumA += p[pos];
            } else {
                sumB += p[pos];
            }
        }

        ans = min(ans, abs(sumA - sumB));
    }

    cout << ans;

    return 0;
} */


//chessboard and queens: uses diagonal and column approach;
/* int main(){
    vector<string> chessboard(8);
    for(int i =0; i<8; i++)
         cin >> chessboard[i];
    int count =0;
    vector<int> columns(8);
    iota(columns.begin(), columns.end(), 0); 
    do {
        bool valid = true;
        for(int i =0; i<8; i++)
            {if(chessboard[i][columns[i]] != '.')
            {
                valid = false;
                break;
            }}
        vector<bool> diagonalOccupied(15, false);
        for (int i =0; i<8; i++){
            if (diagonalOccupied[i+columns[i]])
            valid = false;
            diagonalOccupied[i+columns[i]] = true;

        }
        for (int i = 0; i<15; i++)
            diagonalOccupied[i] = false;
        for (int i =0; i<8; i++)
            {
            if(diagonalOccupied[i+7-columns[i]])
                valid= false;
            diagonalOccupied[i+7-columns[i]] = true;
        }
        if(valid)
            count++;
        }
    while (next_permutation(columns.begin(), columns.end()));
cout << count;
return 0;
} */




//  distinct numbers

/* int main()
{
int n;
cin >> n;
set<int> s;

for(int i=0; i<n; ++i){
    int x;
    cin >> x;
    s.insert(x);

}
cout<< s.size();

} */

 /*  const int mxN = 2e5;
    int n,m,k, a[mxN], b[mxN];

int main(){
  

    cin>> m >>n>>k;

    for(int i = 0;i<n;++i)
    cin>> a[i];
    for(int j=0;j<m;++j)
    cin>> b[j];
ś
    sort(a, a+n);
    sort(b, b+m);
    int ans = 0;
    for(int i=0, j =0; i<n; ++i){

        while(j<m&&a[i]-b[j]>k)
            ++j;
        if(j<m&& b[j]-a[i]<=k)
            ++ans, ++j;
                }
                cout << ans;
}  *//* 
#include <bits/stdc++.h>

using namespace std;

const int maxn = 2e5 + 10;

// Variables used for the current problem
int n, x, p[maxn], i, j, ans;
// Keeps track of the number of children who have had their own gondola
bool have_gondola_yet[maxn];

void solve() {
	cin >> n >> x;
	for (int i = 0; i < n; ++i) cin >> p[i];
	sort(p, p + n);
	i = 0;
	j = n - 1;
	while (i < j) {
		if (p[i] + p[j] > x) {
			// If the total weight of two children exceeds x
			// Then we move to the lighter child.
			--j;
		} else {    // If it satisfies the condition.
			++ans;  // Increment the number of gondolas used
			// Mark that they have had their gondola
			have_gondola_yet[i] = have_gondola_yet[j] = true;
			++i;
			--j;  // Move to the next children.
		}
	}
	for (int i = 0; i < n; ++i) {
		// Calculate the number of children not having gondolas yet
		// to get the total number of gondolas needed for the problem.
		ans += have_gondola_yet[i] == false;
	}
	cout << ans << "\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	solve();
	return 0;
} *//* 
 int main(){

    int n;
    cin>> n;

    vector<pair<int, int>> events;

    for(int i=0; i<n; ++i){
        int arrival, departure;
        cin>> arrival>> departure;
        
        events.push_back({arrival, 1});
        events.push_back({departure, -1});
    }
    sort(events.begin(), events.end());

int curr_count = 0;
int max_count = 0;

    for(auto i: events){
        curr_count+= i.second;

        if(curr_count>max_count){
            max_count = curr_count;

        }

    }
    cout << max_count;
 } */

/*  #include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Define a movie as a pair of start time and end time
typedef pair<int, int> movie;

int main() {
    int n;
    cin >> n;
    vector<movie> movies(n);

    // Read the start and end times of the movies
    for (int i = 0; i < n; ++i) {
        int start, end;
        cin >> start >> end;
        movies[i] = {end, start}; // Store end time first for easier sorting
    }

    // Sort movies by their end times
    sort(movies.begin(), movies.end());

    int count = 0;
    int last_end_time = 0;

    // Select movies greedily
    for (const auto& m : movies) {
        if (m.second >= last_end_time) { // m.second is the start time
            count++;
            last_end_time = m.first; // m.first is the end time
        }
    }

    // Output the maximum number of non-overlapping movies
    cout << count << endl;

    return 0;
}
 */

int main(){
    int n;
long long sum =0;
const int CUSTOM_MIN = -1000000;
int minValue = CUSTOM_MIN;

    cin>> n;
    vector<long long> val(n);

    for(int i=0; i<n; ++i){
        cin>> value[i];

        sum += val[i];
    }
    for(int i =0; i<n; ++i){
        sum += val[i];
        if(max_sum< sum)
            max_sum = sum;

        if(sum < 0)
            sum = 0;
    
    } return max_sum; 
} 

/* #define ll long long ;
int main(){
   long long n,  median;
    cin >> n;
    vector<long long> p(n);
    for( int i=0; i<n; ++i){
        cin>> p[i];
        
    }
    sort(p.begin(), p.end());
    median = p[n/2];
    long long ans = 0;
    for(int i= 0 ; i<n; ++i){
       
        ans+= abs(median -p[i]);


    }
    cout<< ans;
    return 0;
} */
