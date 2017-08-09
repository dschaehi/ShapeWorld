from shapeworld.dataset import CaptionAgreementDataset
from shapeworld.generators import GenericGenerator
from shapeworld.captioners import AttributesNounCaptioner


class OneshapeSimpleDataset(CaptionAgreementDataset):

    dataset_name = 'oneshape_simple'

    def __init__(self, validation_combinations, test_combinations, caption_size, words, hypernym_ratio=None, incorrect_caption_distribution=None, correct_ratio=None, train_correct_ratio=None, validation_correct_ratio=None, test_correct_ratio=None, realizer=None, language=None, world_size=None, world_color=None, shapes=None, colors=None, textures=None, rotation=None, size_range=None, distortion_range=None, shade_range=None, collision_tolerance=None, boundary_tolerance=None, **kwargs):
        world_generator = GenericGenerator([1], world_size, world_color, shapes, colors, textures, rotation, size_range, distortion_range, shade_range, collision_tolerance, boundary_tolerance, validation_combinations=validation_combinations, test_combinations=test_combinations)
        world_captioner = AttributesNounCaptioner(
            hypernym_ratio=hypernym_ratio,
            incorrect_distribution=incorrect_caption_distribution
        )
        super(OneshapeSimpleDataset, self).__init__(
            world_generator=world_generator,
            world_captioner=world_captioner,
            caption_size=caption_size,
            words=words,
            incorrect_world_ratio=0.0,
            correct_ratio=correct_ratio,
            train_correct_ratio=correct_ratio,
            validation_correct_ratio=validation_correct_ratio,
            test_correct_ratio=test_correct_ratio,
            caption_realizer=realizer,
            realizer_language=language
        )


dataset = OneshapeSimpleDataset
OneshapeSimpleDataset.default_config = {
    'validation_combinations': [['square', 'red', 'solid'], ['triangle', 'green', 'solid'], ['circle', 'blue', 'solid']],
    'test_combinations': [['rectangle', 'yellow', 'solid'], ['cross', 'magenta', 'solid'], ['ellipse', 'cyan', 'solid']],
    'caption_size': 6,
    'words': ['.', 'a', 'an', 'black', 'blue', 'circle', 'cross', 'cyan', 'ellipse', 'green', 'is', 'magenta', 'pentagon', 'rectangle', 'red', 'semicircle', 'shape', 'square', 'there', 'triangle', 'white', 'yellow']
}
