class Solution {
    public int[] solution(String[] park, String[] routes) {
        int w = -1;
        int h = -1;
        
        int park_w = park[0].length();
        int park_h = park.length;
        
        int[] answer = new int[2];
        
        for (int i = 0; i < park_w ; i ++) {
            if (park[i].contains("S")) {
                w = park[i].indexOf("S");
                h = i;
            }
        }
        
        for (String route: routes) {
            String[] separ = route.split(" ");
            String compass = separ[0];
            int distance = Integer.parseInt(separ[1]);
            int cur_w = w;
            int cur_h = h;
            if (compass.equals("E")) {
                boolean flag = true;
                for (int i = 0; i < distance ; i++) {
                    cur_w++;
                    if (cur_w >= park_w) {
                        flag = false;
                        break;
                    }
                    if (park[cur_h].charAt(cur_w) =='X') {
                        flag = false;
                        break;
                    }
                }
                if (flag) w = cur_w;
            } else if (compass.equals("W")) {
                boolean flag = true;
                for (int i = 0; i < distance ; i++) {
                    cur_w--;
                    if (cur_w < 0) {
                        flag = false;
                        break;
                    }
                    if (park[cur_h].charAt(cur_w) =='X') {
                        flag = false;
                        break;
                    }
                }
                if (flag) w = cur_w;
            } else if (compass.equals("N")) {
                boolean flag = true;
                for (int i = 0; i < distance ; i++) {
                    cur_h--;
                    if (cur_h < 0) {
                        flag = false;
                        break;
                    }
                    if (park[cur_h].charAt(cur_w) =='X') {
                        flag = false;
                        break;
                    }
                }
                if (flag) h = cur_h;
            } else if (compass.equals("S")) {
                boolean flag = true;
                for (int i = 0; i < distance ; i++) {
                    cur_h++;
                    if (cur_h >= park_h) {
                        flag = false;
                        break;
                    }
                    if (park[cur_h].charAt(cur_w) =='X') {
                        flag = false;
                        break;
                    }
                }
                if (flag) h = cur_h;
            }
        }
        
        answer[0] = h;
        answer[1] = w;
        return answer;
    }
}