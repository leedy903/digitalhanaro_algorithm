package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class Node {
    Map<Character, Node> children = new HashMap<Character, Node>();
    boolean isTerminal = false;
}

class Trie {
    Node root;

    Trie() {
        root = new Node();
    }

    void insert(String word) {
        Node cur = this.root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new Node());
            }
            cur = cur.children.get(c);
        }
        cur.isTerminal = true;
    }

    boolean isConsistent(String word) {
        Node cur = this.root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (cur.isTerminal) return false;
            cur = cur.children.get(c);
        }
        return true;
    }

    void showTree(Node cur, int depth) {
        if (cur.children.isEmpty()) {
            for (int i = 0; i < depth * 2; i++) {
                System.out.print("-");
            }
            System.out.println("terminal " + cur.isTerminal);
        }
        for (char c : cur.children.keySet()) {
            for (int i = 0; i < depth * 2; i++) {
                System.out.print("-");
            }
            System.out.println(c + " " + cur.isTerminal);
            showTree(cur.children.get(c), depth + 1);
        }
    }
}


public class G4_5052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int test_case = 0; test_case < t; test_case++) {
            Trie trie = new Trie();
            String answer = "YES";

            int n = Integer.parseInt(br.readLine());
            String[] phoneNumbers = new String[n];

            for (int i = 0; i < n; i++) {
                String phoneNumber = br.readLine();
                phoneNumbers[i] = phoneNumber;
                trie.insert(phoneNumber);

                System.out.println("\ninsert " + phoneNumber);
                trie.showTree(trie.root, 0);
            }



            for (int i = 0; i < n; i++) {
                String phoneNumber = phoneNumbers[i];
                if (!trie.isConsistent(phoneNumber)) {
                    answer = "NO";
                    break;
                }
            }
            sb.append(answer).append("\n");
        }
        System.out.print(sb);
        br.close();
    }
}
