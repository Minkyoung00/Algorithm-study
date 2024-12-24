package algorithm.dec;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class d25_boj4542 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int size = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < size; i++) {
            String[] array = br.readLine().split(" ");
            if (Integer.parseInt(array[0]) == 0) {
                if (pq.isEmpty())
                    sb.append(-1).append("\n");
                else
                    sb.append(pq.poll()).append("\n");

            } else {
                for (int j = 1 ; j < array.length; j++) {
                    pq.add(Integer.parseInt(array[j]));
                }
            }
        }

        System.out.println(sb);
    }
}
