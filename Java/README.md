## 입출력

### BufferedReader
```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
int n = Integer.parseInt(br.readLine());
```
`BufferedReader`의 `readLine`은 `String`이 기본타입이기에 조건에 맞는 타입으로 형변환을 해주어야 사용이 가능하다.

### StringTokenizer
```java
StringTokenizer st = new StringTokenizer(br.readLine());
String mod = st.nextToken();
```
입력 방식이 `3 3`과 같이 2개 이상의 값을 넣을 때는 `Tokenizer`를 사용한다.  
> 다만 BFS 보드 삽입처럼 갯수가 많아질 때는 사용하지 않는게 좋겠다.  

### StringBuilder
```java
StringBuilder sb = new StringBuilder();
sb.append("a");
sb.append("b").append(" ");
sb.append("c").append("\n");
System.out.println(sb); // ab c
```
자주 사용되는 Java 출력이라고 한다.

## Stack
```java
Stack<Integer> stack = new Stack<>();

stack.push(1); // 1 추가
stack.pop(); // top 삭제
stack.clear(); // stack 초기화
stack.size(); // 스택 크기 반환
stack.empty(); // isEmpty()랑 뭐가 다르지
stack.cotains(1); // 1이 포함되어 있으면 true, 없으면 false
stack.peek() // top 출력 (제거X), 비어있으면 null 반환
```