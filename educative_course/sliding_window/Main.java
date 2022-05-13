import java.util.ArrayList;

class Main {

    public boolean colorInDfs(int node,  ArrayList<ArrayList<Integer>> adj, int[] color){
        return true;
    }

    boolean checkDFS(ArrayList<ArrayList<Integer>> adj, int n){
        int color[] = new int[n];
        for(int i = 0; i < n; i++){
            color[i] = -1;
        }
        for(int it : color){
            if(it == -1) {
               if(!colorInDfs(it, adj, color)) return false;
            }
        }
        return true;
    }

    public static void main(String args[]){
        int noOfNodes = 7;

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();

        for(int i = 0; i < noOfNodes; i++){
            adj.add(new ArrayList<>());
        }

        Main inst = new Main();

        System.out.println(inst.checkDFS(adj, noOfNodes));
    }
}

