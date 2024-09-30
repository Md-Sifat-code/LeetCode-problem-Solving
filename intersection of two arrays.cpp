class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> vex;
        vector<int> vex1;
        vector<int> vex3;

        for (int i = 0; i < nums1.size(); i++) {
            bool found = false;
            for (int j = 0; j < vex.size(); j++) {
                if (vex[j] == nums1[i]) {
                    found = true;
                    break;
                }
            }
            if (!found) vex.push_back(nums1[i]);
        }

        for (int i = 0; i < nums2.size(); i++) {
            bool found = false;
            for (int j = 0; j < vex1.size(); j++) {
                if (vex1[j] == nums2[i]) {
                    found = true;
                    break;
                }
            }
            if (!found) vex1.push_back(nums2[i]);
        }

        if (vex1.size() < vex.size()) {
            for (int i = 0; i < vex1.size(); i++) {
                for (int j = 0; j < vex.size(); j++) {
                    if (vex1[i] == vex[j]) {
                        vex3.push_back(vex1[i]);
                        break;
                    }
                }
            }
        } else {
            for (int i = 0; i < vex.size(); i++) {
                for (int j = 0; j < vex1.size(); j++) {
                    if (vex[i] == vex1[j]) {
                        vex3.push_back(vex[i]);
                        break;
                    }
                }
            }
        }
        return vex3;
    }
};
