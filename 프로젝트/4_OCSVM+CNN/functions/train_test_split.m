function [data_tr, data_te,label_tr, label_te] = train_test_split(X,y,p)
[m,~] = size(X);
if m == length(y)
    idx = randperm(m)  ;
    data_tr = X(idx(1:round(p*m)),:);
    data_te = X(idx(round(p*m)+1:end),:);
    
    label_tr = y(idx(1:round(p*m)));
    label_te = y(idx(round(p*m)+1:end));
else
    disp('check your data')
    
end
end

