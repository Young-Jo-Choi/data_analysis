function tbl_count = value_counts(A)
[C, ia, ic] = unique(A);
a_counts = accumarray(ic,1);
tbl_count = table(C, a_counts,'VariableNames',["항목","개수"]);
end