# 자바 코딩테스트 준비
## Package
```java
import java.util.*;
import java.io.*;
```
두 패키지를 모두 import해서 사용하면 조금 더 수월하게 사용이 가능하다.  
다만 기업마다 import 선언문을 확실시하는 곳도 했던 것 같으므로 어느정도는 알아두는 것이 편하다.

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

## Queue
```java
Queue<Integer> queue = new LinkedList<>();

queue.add(1); // 값 추가 - Queue가 꽉 차있다면 exception 발생.
queue.offer(2); // 값 추가 - Queue가 꽉 차있다면 return 값은 false임.
queue.poll(); // 첫 번째 값 반환 (제거됨), 비어있다면 null 반환
queue.remove(); // 첫 번째 값 삭제
queue.clear(); // Queue Clear
queue.peek(); // 첫 번째 값 반환 (제거X)
```