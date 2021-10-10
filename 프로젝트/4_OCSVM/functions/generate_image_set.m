function [imds_set, label_set] = generate_image_set(path)
% 여러 imds를 하나의 structure로 만들어준다.

imds_set = {};
imds = imageDatastore(path,"IncludeSubfolders",true,'LabelSource',"foldernames");
label_set = unique(imds.Labels);

for i=1:length(label_set)
    new_path = strcat(path,'\',string(label_set(i)));
    command = strcat('imds_temp=imageDatastore(new_path,"IncludeSubfolders",true,"LabelSource","foldernames");');
    eval(command);
    imds_set{i} = imds_temp;
end

end

