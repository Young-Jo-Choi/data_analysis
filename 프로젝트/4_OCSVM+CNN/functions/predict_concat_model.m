function pred = predict_concat_model(net, classifiers, set_want_to_predict,label_set,featureLayer)

imageSize = net.Layers(1).InputSize;


augmentedTest= augmentedImageDatastore(imageSize, set_want_to_predict);
testFeatures = activations(net, augmentedTest, featureLayer, ...
    'MiniBatchSize', 32, 'OutputAs', 'columns');

tbl = table();
for i=1:length(classifiers)
    [~,scores] = predict(classifiers{i},testFeatures,'ObservationsIn', 'columns');    
    tbl = addvars(tbl,scores,'NewVariableNames',string(label_set(i)));

end


pred = addvars(tbl,set_want_to_predict.Labels,'NewVariableNames','class');
end

