function classifiers = train_concat_model(net,imds_set,featureLayer)
% each element of imds_set has one class labeling
imageSize = net.Layers(1).InputSize;
classifiers = {};
for i=1:length(imds_set)
    augmentedTrainingSet = augmentedImageDatastore(imageSize, imds_set{i});
    trainingFeatures = activations(net, augmentedTrainingSet, featureLayer, ...
        'MiniBatchSize', 32, 'OutputAs', 'columns');
    trainingFeatures = trainingFeatures';
    trainingLabels = imds_set{i}.Labels;
    
    temp_classifier = fitcsvm(trainingFeatures,trainingLabels,"KernelScale","auto","Standardize",true,"OutlierFraction",0.05);
    classifiers{i} = temp_classifier;
end

end

