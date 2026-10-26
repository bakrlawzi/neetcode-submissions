class Solution {

    public String encode(List<String> strs) {
           StringBuilder w = new StringBuilder();
        for (String str : strs) {
            w.append(str.length()).append(":").append(str);
        }
        return w.toString();
    }

    public List<String> decode(String str) {
            List<String> L = new ArrayList<>();
        int i = 0;
        while (i < str.length()) {
            // Find the length prefix
            int colon = str.indexOf(":", i);
            int length = Integer.parseInt(str.substring(i, colon));

            // Extract the substring of the given length
            String decodedStr = str.substring(colon + 1, colon + 1 + length);
            L.add(decodedStr);

            // Move the pointer to the next encoded string
            i = colon + 1 + length;
        }
        return L;
    }
}
